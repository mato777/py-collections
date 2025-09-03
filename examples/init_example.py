#!/usr/bin/env python3
"""
Example demonstrating Collection initialization methods.
"""

from py_collections import Collection


def main():
    """Demonstrate Collection initialization functionality."""
    
    print("=== Collection Initialization Examples ===\n")
    
    # Initialize with an existing array
    print("1. Initialize with existing array:")
    my_array = [1, 2, 3]
    collection = Collection(my_array)
    print(f"   Original array: {my_array}")
    print(f"   Collection: {collection}")
    print(f"   Length: {len(collection)}\n")
    
    # Initialize empty collection
    print("2. Initialize empty collection:")
    empty_collection = Collection()
    print(f"   Empty collection: {empty_collection}")
    print(f"   Length: {len(empty_collection)}")
    
    empty_collection.append("hello")
    empty_collection.append("world")
    print(f"   After appending: {empty_collection}\n")
    
    # Collection independence
    print("3. Collection independence:")
    collection1 = Collection([1, 2, 3])
    collection2 = Collection([4, 5, 6])
    
    collection1.append(7)
    collection2.append(8)
    
    print(f"   Collection 1: {collection1}")
    print(f"   Collection 2: {collection2}")
    print("   ✓ Collections are independent!")


if __name__ == "__main__":
    main()
