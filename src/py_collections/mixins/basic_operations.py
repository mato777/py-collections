"""Basic operations mixin for Collection class."""

from typing import Any, TypeVar, Union

from py_collections.collection import Collection

T = TypeVar("T")


class BasicOperationsMixin[T]:
    """Mixin providing basic collection operations."""

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
        if hasattr(items, "_items"):  # Check if it's a Collection-like object
            self._items.extend(items._items)
        else:
            self._items.extend(items)

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
