from collections.abc import Callable
from typing import Any, TypeVar, Union


class ItemNotFoundException(Exception):
    """Exception raised when an item is not found in the collection."""


T = TypeVar("T")


class Collection[T]:
    """
    A collection class that wraps a list and provides methods to manipulate it.

    Args:
        items: Optional list of items to initialize the collection with.
               If not provided, an empty list will be used.
    """

    def __init__(self, items: list[T] | None = None):
        self._items = items.copy() if items is not None else []

    def append(self, item: T) -> None:
        """
        Append an item to the collection.

        Args:
            item: The item to append to the collection.
        """
        self._items.append(item)

    def extend(self, items: Union[list[T], "Collection[T]"]) -> None:
        """
        Extend the collection with items from a list or another collection.

        Args:
            items: A list or Collection containing items to add to the current collection.
        """
        if isinstance(items, Collection):
            self._items.extend(items._items)
        else:
            self._items.extend(items)

    def reverse(self) -> "Collection[T]":
        """
        Return a new collection with the items reversed in order.

        Returns:
            A new Collection containing the items in reverse order.
        """
        reversed_items = self._items[::-1]
        return Collection(reversed_items)

    def clone(self) -> "Collection[T]":
        """
        Return a new collection with the same items.

        Returns:
            A new Collection containing the same items as the original.
        """
        return Collection(self._items.copy())

    def remove(self, target: T | Callable[[T], bool]) -> None:
        """
        Remove all items that match the target element or predicate.

        Args:
            target: Either an element to remove, or a callable that takes an item and returns a boolean.
                   If an element is provided, removes all occurrences of that element.
                   If a callable is provided, removes all elements that satisfy the predicate.
        """
        if callable(target):
            predicate = target
            self._items[:] = [item for item in self._items if not predicate(item)]
        else:
            self._items[:] = [item for item in self._items if item != target]

    def remove_one(self, target: T | Callable[[T], bool]) -> None:
        """
        Remove the first occurrence of an item that matches the target element or predicate.

        Args:
            target: Either an element to remove, or a callable that takes an item and returns a boolean.
                   If an element is provided, removes the first occurrence of that element.
                   If a callable is provided, removes the first element that satisfies the predicate.
        """
        if not self._items:
            return

        if callable(target):
            predicate = target
            for i, item in enumerate(self._items):
                if predicate(item):
                    del self._items[i]
                    return
        else:
            try:
                self._items.remove(target)
            except ValueError:
                # Element not found, do nothing
                pass

    def first(self, predicate: Callable[[T], bool] | None = None) -> T | None:
        """
        Get the first element in the collection.

        Args:
            predicate: Optional callable that takes an item and returns a boolean.
                      If provided, returns the first element that satisfies the predicate.
                      If None, returns the first element in the collection.

        Returns:
            The first element that satisfies the predicate, or the first element if no predicate is provided.
            Returns None if the collection is empty or no element satisfies the predicate.
        """
        index = self._find_first_index(predicate)
        return self._items[index] if index is not None else None

    def exists(self, predicate: Callable[[T], bool] | None = None) -> bool:
        """
        Check if an element exists in the collection.

        Args:
            predicate: Optional callable that takes an item and returns a boolean.
                      If provided, checks if any element satisfies the predicate.
                      If None, checks if the collection is not empty.

        Returns:
            True if an element exists that satisfies the predicate (or if collection is not empty when no predicate),
            False otherwise.
        """
        return self._find_first_index(predicate) is not None

    def _find_first_index(
        self, predicate: Callable[[T], bool] | None = None
    ) -> int | None:
        """
        Find the index of the first element that satisfies the predicate.

        Args:
            predicate: Optional callable that takes an item and returns a boolean.
                      If None, returns 0 (first element).

        Returns:
            Index of the first matching element, or None if not found.
        """
        if not self._items:
            return None

        if predicate is None:
            return 0

        for i, item in enumerate(self._items):
            if predicate(item):
                return i

        return None

    def first_or_raise(self, predicate: Callable[[T], bool] | None = None) -> T:
        """
        Get the first element in the collection or raise ItemNotFoundException if not found.

        Args:
            predicate: Optional callable that takes an item and returns a boolean.
                      If provided, returns the first element that satisfies the predicate.
                      If None, returns the first element in the collection.

        Returns:
            The first element that satisfies the predicate, or the first element if no predicate is provided.

        Raises:
            ItemNotFoundException: If the collection is empty or no element satisfies the predicate.
        """
        index = self._find_first_index(predicate)
        if index is None:
            if not self._items:
                raise ItemNotFoundException(
                    "Cannot get first element from empty collection"
                )
            else:
                raise ItemNotFoundException("No element satisfies the predicate")
        return self._items[index]

    def after(self, target: T | Callable[[T], bool]) -> T | None:
        """
        Get the element that comes after the first occurrence of the target element or predicate match.

        Args:
            target: Either an element to search for, or a callable that takes an item and returns a boolean.
                   If an element is provided, searches for the first occurrence of that element.
                   If a callable is provided, searches for the first element that satisfies the predicate.

        Returns:
            The element that comes after the matched element, or None if no match is found or if the match
            is the last element in the collection.
        """
        if not self._items:
            return None

        # Handle case where target is a callable (predicate)
        if callable(target):
            predicate = target
            for i, item in enumerate(self._items):
                if predicate(item):
                    # Check if there's a next element
                    if i + 1 < len(self._items):
                        return self._items[i + 1]
                    return None
            return None

        # Handle case where target is an element
        try:
            index = self._items.index(target)
            # Check if there's a next element
            if index + 1 < len(self._items):
                return self._items[index + 1]
            return None
        except ValueError:
            # Element not found
            return None

    def before(self, target: T | Callable[[T], bool]) -> T | None:
        """
        Get the element that comes before the first occurrence of the target element or predicate match.

        Args:
            target: Either an element to search for, or a callable that takes an item and returns a boolean.
                   If an element is provided, searches for the first occurrence of that element.
                   If a callable is provided, searches for the first element that satisfies the predicate.

        Returns:
            The element that comes before the matched element, or None if no match is found or if the match
            is the first element in the collection.
        """
        if not self._items:
            return None

        # Handle case where target is a callable (predicate)
        if callable(target):
            predicate = target
            for i, item in enumerate(self._items):
                if predicate(item):
                    # Check if there's a previous element
                    if i > 0:
                        return self._items[i - 1]
                    return None
            return None

        # Handle case where target is an element
        try:
            index = self._items.index(target)
            # Check if there's a previous element
            if index > 0:
                return self._items[index - 1]
            return None
        except ValueError:
            # Element not found
            return None

    def filter(self, predicate: Callable[[T], bool]) -> "Collection[T]":
        """
        Filter the collection based on a predicate function.

        Args:
            predicate: A callable that takes an item and returns a boolean.
                      Items that return True will be included in the filtered collection.

        Returns:
            A new Collection containing only the elements that satisfy the predicate.
        """
        filtered_items = [item for item in self._items if predicate(item)]
        return Collection(filtered_items)

    def group_by(
        self, key: str | Callable[[T], Any] | None = None
    ) -> dict[Any, "Collection[T]"]:
        """
        Group the collection's items by a given key or callback function.

        Args:
            key: Either a string representing an attribute/key to group by,
                 or a callable that takes an item and returns the grouping key.
                 If None, groups by the item itself.

        Returns:
            A dictionary where keys are the grouping values and values are Collection
            instances containing the grouped items.

        Examples:
            # Group by attribute
            users.group_by('department')

            # Group by callback function
            users.group_by(lambda user: user.age // 10 * 10)  # Group by age decade

            # Group by item itself
            numbers.group_by()  # Groups identical numbers together
        """
        if not self._items:
            return {}

        grouped = {}

        for item in self._items:
            if key is None:
                # Group by the item itself
                group_key = item
            elif isinstance(key, str):
                # Group by attribute/key (for dictionaries or objects)
                if isinstance(item, dict):
                    group_key = item.get(key)
                else:
                    group_key = getattr(item, key, None)
            elif callable(key):
                # Group by callback function
                group_key = key(item)
            else:
                raise ValueError("Key must be a string, callable, or None")

            # Convert key to hashable type for dictionary keys
            if isinstance(group_key, list | dict | set):
                group_key = str(group_key)

            if group_key not in grouped:
                grouped[group_key] = Collection()

            grouped[group_key].append(item)

        return grouped

    def chunk(self, size: int) -> list["Collection[T]"]:
        """
        Split the collection into smaller collections of the specified size.

        Args:
            size: The size of each chunk. Must be a positive integer.

        Returns:
            A list of Collection objects, each containing up to 'size' elements.
            The last chunk may contain fewer elements if the total number of elements
            is not evenly divisible by the chunk size.

        Raises:
            ValueError: If size is not a positive integer.
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Chunk size must be a positive integer")

        if not self._items:
            return []

        chunks = []
        for i in range(0, len(self._items), size):
            chunk_items = self._items[i : i + size]
            chunks.append(Collection(chunk_items))

        return chunks

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

    def last(self) -> T:
        """
        Get the last element in the collection.

        Returns:
            The last element in the collection.

        Raises:
            IndexError: If the collection is empty.
        """
        if not self._items:
            raise IndexError("Cannot get last element from empty collection")
        return self._items[-1]

    def all(self) -> list[T]:
        """
        Get all items in the collection as a list.

        Returns:
            A list containing all items in the collection.
        """
        return self._items.copy()

    def __len__(self) -> int:
        """Return the number of items in the collection."""
        return len(self._items)

    def __iter__(self):
        """
        Return an iterator over the collection's items.

        Returns:
            An iterator that yields each item in the collection.
        """
        return iter(self._items)

    def __str__(self) -> str:
        """Return a string representation of the collection."""
        return f"Collection({self._items})"

    def __repr__(self) -> str:
        """Return a detailed string representation of the collection."""
        return f"Collection({self._items})"
