#!/usr/bin/env python3
"""
Example demonstrating Collection first and last methods.
"""

from py_collections import Collection


def main():
    """Demonstrate Collection first and last functionality."""
    
    print("=== Collection First and Last Examples ===\n")
    
    # Basic first and last functionality
    print("1. Basic first and last functionality:")
    numbers = Collection([10, 20, 30, 40, 50])
    print(f"   Collection: {numbers}")
    print(f"   First element: {numbers.first()}")
    print(f"   Last element: {numbers.last()}\n")
    
    # First with predicate functionality
    print("2. First with predicate functionality:")
    print(f"   First even number: {numbers.first(lambda x: x % 2 == 0)}")
    print(f"   First number > 25: {numbers.first(lambda x: x > 25)}")
    print(f"   First number divisible by 10: {numbers.first(lambda x: x % 10 == 0)}\n")
    
    # First and last after append
    print("3. First and last after append:")
    numbers.append(60)
    print(f"   After appending 60: {numbers}")
    print(f"   First element still: {numbers.first()}")
    print(f"   Last element now: {numbers.last()}\n")
    
    # First and last with different types
    print("4. First and last with different types:")
    mixed = Collection(["apple", 42, {"key": "value"}])
    print(f"   Mixed collection: {mixed}")
    print(f"   First element: {mixed.first()}")
    print(f"   Last element: {mixed.last()}\n")
    
    # Single element (first and last should be the same)
    print("5. Single element collection:")
    single = Collection([999])
    print(f"   Single element collection: {single}")
    print(f"   First and last are the same: {single.first()} == {single.last()}\n")
    
    # Empty collection (will raise error)
    print("6. Empty collection first and last elements:")
    empty = Collection()
    try:
        first = empty.first()
        print(f"   First element: {first}")
    except IndexError as e:
        print(f"   First error: {e}")
    
    try:
        last = empty.last()
        print(f"   Last element: {last}")
    except IndexError as e:
        print(f"   Last error: {e}")


if __name__ == "__main__":
    main()
