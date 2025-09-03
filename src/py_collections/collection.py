from typing import List, Any, TypeVar, Generic, Callable


class ItemNotFoundException(Exception):
    """Exception raised when an item is not found in the collection."""
    pass


T = TypeVar('T')


class Collection(Generic[T]):
    """
    A collection class that wraps a list and provides methods to manipulate it.
    
    Args:
        items: Optional list of items to initialize the collection with.
               If not provided, an empty list will be used.
    """
    
    def __init__(self, items: List[T] = None):
        self._items = (items.copy() if items is not None else [])
    
    def append(self, item: T) -> None:
        """
        Append an item to the collection.
        
        Args:
            item: The item to append to the collection.
        """
        self._items.append(item)
    
    def first(self, predicate: Callable[[T], bool] = None) -> T | None:
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
    
    def _find_first_index(self, predicate: Callable[[T], bool] = None) -> int | None:
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
    
    def first_or_raise(self, predicate: Callable[[T], bool] = None) -> T:
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
                raise ItemNotFoundException("Cannot get first element from empty collection")
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
    
    def filter(self, predicate: Callable[[T], bool]) -> 'Collection[T]':
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
    
    def chunk(self, size: int) -> List['Collection[T]']:
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
            chunk_items = self._items[i:i + size]
            chunks.append(Collection(chunk_items))
        
        return chunks
    
    def dump_me(self) -> None:
        """
        Stop execution and print all elements in the collection for debugging.
        
        This method is useful for debugging purposes. It will:
        1. Print the collection's string representation
        2. Print each element individually with its index
        3. Print the total number of elements
        4. Stop execution by raising a SystemExit exception
        
        Raises:
            SystemExit: Always raises this exception to stop execution.
        """
        print(f"\n=== Collection Dump ===")
        print(f"Collection: {self}")
        print(f"Type: {type(self)}")
        print(f"Length: {len(self._items)}")
        print(f"Elements:")
        
        if not self._items:
            print("  (empty collection)")
        else:
            for i, item in enumerate(self._items):
                print(f"  [{i}]: {item} (type: {type(item).__name__})")
        
        print(f"=== End Collection Dump ===\n")
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
    
    def all(self) -> List[T]:
        """
        Get all items in the collection as a list.
        
        Returns:
            A list containing all items in the collection.
        """
        return self._items.copy()
    
    def __len__(self) -> int:
        """Return the number of items in the collection."""
        return len(self._items)
    
    def __str__(self) -> str:
        """Return a string representation of the collection."""
        return f"Collection({self._items})"
    
    def __repr__(self) -> str:
        """Return a detailed string representation of the collection."""
        return f"Collection({self._items})"
