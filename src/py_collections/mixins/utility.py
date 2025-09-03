"""Utility mixin for Collection class."""

from typing import TypeVar

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
