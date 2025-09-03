#!/usr/bin/env python3
"""
Example demonstrating Collection edge cases and error handling.
"""

from py_collections import Collection


def main():
    """Demonstrate Collection edge cases and error handling."""
    
    print("=== Collection Edge Cases and Error Handling ===\n")
    
    # Empty collection operations
    print("1. Empty collection operations:")
    empty = Collection()
    print(f"   Empty collection: {empty}")
    print(f"   Length: {len(empty)}")
    print(f"   All items: {empty.all()}")
    
    try:
        first = empty.first()
        print(f"   First element: {first}")
    except IndexError as e:
        print(f"   First error: {e}")
    
    try:
        last = empty.last()
        print(f"   Last element: {last}")
    except IndexError as e:
        print(f"   Last error: {e}\n")
    
    # Single element collection
    print("2. Single element collection:")
    single = Collection([999])
    print(f"   Single element collection: {single}")
    print(f"   Length: {len(single)}")
    print(f"   First element: {single.first()}")
    print(f"   Last element: {single.last()}")
    print(f"   First == Last: {single.first() == single.last()}\n")
    
    # Collection with None values
    print("3. Collection with None values:")
    none_collection = Collection([None, "hello", None, 42])
    print(f"   None collection: {none_collection}")
    print(f"   First element: {none_collection.first()}")
    print(f"   Last element: {none_collection.last()}")
    print(f"   All items: {none_collection.all()}\n")
    
    # Collection with empty lists/dicts
    print("4. Collection with empty containers:")
    empty_containers = Collection([[], {}, "", 0])
    print(f"   Empty containers collection: {empty_containers}")
    print(f"   First element: {empty_containers.first()}")
    print(f"   Last element: {empty_containers.last()}\n")
    
    # Collection independence (deep copy behavior)
    print("5. Collection independence:")
    original_list = [1, 2, 3]
    collection1 = Collection(original_list)
    collection2 = Collection(original_list)
    
    # Modify original list
    original_list.append(999)
    print(f"   Original list modified: {original_list}")
    print(f"   Collection 1 unchanged: {collection1}")
    print(f"   Collection 2 unchanged: {collection2}")
    print("   ✓ Collections are independent of original list!")
    
    # Modify collection
    collection1.append(888)
    print(f"   Collection 1 modified: {collection1}")
    print(f"   Collection 2 unchanged: {collection2}")
    print("   ✓ Collections are independent of each other!")


if __name__ == "__main__":
    main()
