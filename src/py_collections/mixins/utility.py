"""Utility mixin for Collection class."""

from typing import Any, TypeVar

from py_collections.collection import Collection

T = TypeVar("T")


class UtilityMixin[T]:
    """Mixin providing utility methods."""

    def take(self, count: int) -> "Collection[T]":
        """
        Return a new collection with the specified number of items.

        Args:
            count: The number of items to take. If positive, takes from the beginning.
                   If negative, takes from the end. If count exceeds the collection size,
                   returns all available items.

        Returns:
            A new Collection containing the specified number of items.

        Examples:
            collection = Collection([1, 2, 3, 4, 5])
            collection.take(2).all()  # [1, 2]
            collection.take(-2).all()  # [4, 5]
            collection.take(10).all()  # [1, 2, 3, 4, 5] (all items)
        """
        from ..collection import Collection

        if not self._items:
            return Collection()

        taken_items = self._items[:count] if count >= 0 else self._items[count:]
        return Collection(taken_items)

    def dump_me(self) -> None:
        """
        Print all elements in the collection for debugging without stopping execution.

        This method is useful for debugging purposes. It will:
        1. Print the collection's string representation
        2. Print each element individually with its index
        3. Print the total number of elements

        Returns:
            None
        """
        print("\n=== Collection Dump ===")
        print(f"Collection: {self}")
        print(f"Type: {type(self)}")
        print(f"Length: {len(self._items)}")
        print("Elements:")

        if not self._items:
            print("  (empty collection)")
        else:
            for i, item in enumerate(self._items):
                print(f"  [{i}]: {item} (type: {type(item).__name__})")

        print("=== End Collection Dump ===\n")

    def dump_me_and_die(self) -> None:
        """
        Print all elements in the collection for debugging and stop execution.

        This method is useful for debugging purposes. It will:
        1. Print the collection's string representation
        2. Print each element individually with its index
        3. Print the total number of elements
        4. Stop execution by raising a SystemExit exception

        Raises:
            SystemExit: Always raises this exception to stop execution.
        """
        self.dump_me()
        raise SystemExit("Collection dump completed - execution stopped")

    def to_dict(self, mode: str | None = None) -> list["Any"]:
        """
        Return the collection items converted to plain Python structures.

        - Objects are converted to dictionaries (using dataclasses, __dict__, or to_dict if available).
        - Containers (dict, list, tuple, set) are converted recursively.
        - If mode == "json", the result is guaranteed to be JSON-serializable
          (datetimes to ISO strings, Decimals to float, UUIDs to str, sets to lists, etc.).

        Args:
            mode: When set to "json", ensures the returned structure is JSON-serializable.

        Returns:
            A list containing the converted items.
        """

        json_mode = mode == "json"

        def convert(value: "Any") -> "Any":
            # Primitives
            if value is None or isinstance(value, (bool, int, float, str)):
                return value

            # Avoid circular import: import here
            from ..collection import Collection as _Collection

            # Collections
            if isinstance(value, _Collection):
                return [convert(v) for v in value.all()]

            # Built-in containers
            if isinstance(value, (list, tuple)):
                return [convert(v) for v in value]
            if isinstance(value, set):
                # sets are not JSON-serializable; always convert to list for consistency
                return [convert(v) for v in value]
            if isinstance(value, dict):
                # Convert keys to string in json mode (JSON requires string keys)
                if json_mode:
                    return {str(convert(k)): convert(v) for k, v in value.items()}
                return {convert(k): convert(v) for k, v in value.items()}

            # Dataclasses
            try:
                from dataclasses import is_dataclass, asdict  # type: ignore
            except Exception:  # pragma: no cover - defensive
                is_dataclass = None  # type: ignore
                asdict = None  # type: ignore
            if callable(is_dataclass) and is_dataclass(value):  # type: ignore
                data = asdict(value)  # type: ignore
                return convert(data)

            # Pydantic models (v1 and v2)
            # Use duck-typing to avoid hard dependency
            model_dump_fn = getattr(value, "model_dump", None)
            dict_fn = getattr(value, "dict", None)
            if callable(model_dump_fn):
                try:
                    # In v2, mode="json" ensures JSON-safe primitives when requested
                    data = (
                        model_dump_fn(mode="json") if json_mode else model_dump_fn()
                    )
                except TypeError:
                    # Older signatures without mode param
                    data = model_dump_fn()
                return convert(data)
            if callable(dict_fn):
                try:
                    data = dict_fn()
                except TypeError:
                    data = dict_fn
                return convert(data)

            # Third-party/common types handling in json mode
            if json_mode:
                try:
                    import datetime as _dt
                    import decimal as _decimal
                    import uuid as _uuid
                except Exception:  # pragma: no cover - defensive
                    _dt = None  # type: ignore
                    _decimal = None  # type: ignore
                    _uuid = None  # type: ignore

                if _dt and isinstance(value, (_dt.datetime, _dt.date, _dt.time)):
                    # Use ISO format for JSON
                    return value.isoformat()
                if _decimal and isinstance(value, _decimal.Decimal):
                    # Convert Decimal to float for JSON
                    return float(value)
                if _uuid and isinstance(value, _uuid.UUID):
                    return str(value)

            # Objects exposing to_dict()
            if hasattr(value, "to_dict") and callable(getattr(value, "to_dict")):
                try:
                    return convert(value.to_dict())  # type: ignore
                except TypeError:
                    # Some to_dict expect args; fall back to __dict__
                    pass

            # Fallback: use __dict__ if available, else string representation
            if hasattr(value, "__dict__"):
                return {k: convert(v) for k, v in vars(value).items() if not k.startswith("__")}

            # Final fallback: string representation (ensures json serializable when needed)
            return str(value)

        return [convert(item) for item in self._items]

    def to_json(self) -> str:
        """
        Return a JSON string representing the collection items.

        Uses to_dict(mode="json") under the hood and json.dumps to stringify.

        Returns:
            A JSON-formatted string.
        """

        import json

        return json.dumps(self.to_dict(mode="json"), ensure_ascii=False)
