#!/usr/bin/env python3
"""
Example demonstrating Collection append method.
"""

from py_collections import Collection


def main():
    """Demonstrate Collection append functionality."""
    
    print("=== Collection Append Examples ===\n")
    
    # Basic append functionality
    print("1. Basic append functionality:")
    collection = Collection([1, 2, 3])
    print(f"   Initial collection: {collection}")
    print(f"   Length: {len(collection)}")
    
    collection.append(4)
    collection.append(5)
    print(f"   After appending: {collection}")
    print(f"   Length: {len(collection)}\n")
    
    # Append different data types
    print("2. Append different data types:")
    mixed_collection = Collection()
    mixed_collection.append(42)
    mixed_collection.append("string")
    mixed_collection.append([1, 2, 3])
    mixed_collection.append({"key": "value"})
    print(f"   Mixed collection: {mixed_collection}\n")
    
    # Append to empty collection
    print("3. Append to empty collection:")
    empty_collection = Collection()
    print(f"   Empty collection: {empty_collection}")
    print(f"   Length: {len(empty_collection)}")
    
    empty_collection.append("hello")
    empty_collection.append("world")
    print(f"   After appending: {empty_collection}")
    print(f"   Length: {len(empty_collection)}")


if __name__ == "__main__":
    main()
