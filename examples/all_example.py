#!/usr/bin/env python3
"""
Example demonstrating Collection all method.
"""

from py_collections import Collection


def main():
    """Demonstrate Collection all functionality."""
    
    print("=== Collection All Examples ===\n")
    
    # Basic all functionality
    print("1. Basic all functionality:")
    collection = Collection([1, 2, 3, 4, 5])
    all_items = collection.all()
    print(f"   Collection: {collection}")
    print(f"   All items: {all_items}")
    print(f"   Number of items: {len(all_items)}")
    print(f"   All items are copies: {all_items is not collection._items}\n")
    
    # Get all items (returns a copy)
    print("2. Get all items (returns a copy):")
    items = collection.all()
    print(f"   Items: {items}")
    items.append(999)  # This won't affect the original collection
    print(f"   Modified items: {items}")
    print(f"   Original collection unchanged: {collection}\n")
    
    # All items with different types
    print("3. All items with different types:")
    mixed_collection = Collection([42, "string", [1, 2, 3], {"key": "value"}])
    mixed_items = mixed_collection.all()
    print(f"   Mixed collection: {mixed_collection}")
    print(f"   All mixed items: {mixed_items}")
    print(f"   Types: {[type(item).__name__ for item in mixed_items]}\n")
    
    # Empty collection
    print("4. Empty collection:")
    empty_collection = Collection()
    empty_items = empty_collection.all()
    print(f"   Empty collection: {empty_collection}")
    print(f"   All items: {empty_items}")
    print(f"   Length: {len(empty_items)}")


if __name__ == "__main__":
    main()
