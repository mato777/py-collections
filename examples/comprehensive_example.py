#!/usr/bin/env python3
"""
Comprehensive example demonstrating all Collection methods together.
"""

from typing import List
from py_collections import Collection


def main():
    """Demonstrate all Collection functionality in a comprehensive example."""
    
    print("=== Comprehensive Collection Example ===\n")
    
    # 1. Initialize collections
    print("1. Initializing collections:")
    numbers = Collection([1, 2, 3, 4, 5])
    strings = Collection(["apple", "banana"])
    empty = Collection()
    
    print(f"   Numbers: {numbers}")
    print(f"   Strings: {strings}")
    print(f"   Empty: {empty}\n")
    
    # 2. Append operations
    print("2. Append operations:")
    numbers.append(6)
    numbers.append(7)
    strings.append("cherry")
    empty.append("first item")
    
    print(f"   Numbers after append: {numbers}")
    print(f"   Strings after append: {strings}")
    print(f"   Empty after append: {empty}\n")
    
    # 3. First, last, after, filter, first_or_raise, chunk, and dump_me operations
    print("3. First, last, after, filter, first_or_raise, chunk, and dump_me operations:")
    print(f"   Numbers - First: {numbers.first()}, Last: {numbers.last()}")
    print(f"   Strings - First: {strings.first()}, Last: {strings.last()}")
    print(f"   Empty - First: {empty.first()}, Last: {empty.last()}")
    
    # First with predicate examples
    print(f"   Numbers - First even: {numbers.first(lambda x: x % 2 == 0)}")
    print(f"   Numbers - First > 3: {numbers.first(lambda x: x > 3)}")
    print(f"   Strings - First with 'e': {strings.first(lambda s: 'e' in s)}")
    
    # After examples
    print(f"   Numbers - After 2: {numbers.after(2)}")
    print(f"   Numbers - After first even: {numbers.after(lambda x: x % 2 == 0)}")
    print(f"   Strings - After 'banana': {strings.after('banana')}")
    print(f"   Strings - After first with 'e': {strings.after(lambda s: 'e' in s)}")
    
    # Before examples
    print(f"   Numbers - Before 2: {numbers.before(2)}")
    print(f"   Numbers - Before first even: {numbers.before(lambda x: x % 2 == 0)}")
    print(f"   Strings - Before 'banana': {strings.before('banana')}")
    print(f"   Strings - Before first with 'e': {strings.before(lambda s: 'e' in s)}")
    
    # Filter examples
    even_numbers = numbers.filter(lambda x: x % 2 == 0)
    print(f"   Numbers - Even numbers: {even_numbers}")
    long_strings = strings.filter(lambda s: len(s) > 5)
    print(f"   Strings - Long strings: {long_strings}")
    
    # First_or_raise examples
    print(f"   Numbers - First_or_raise even: {numbers.first_or_raise(lambda x: x % 2 == 0)}")
    print(f"   Strings - First_or_raise with 'e': {strings.first_or_raise(lambda s: 'e' in s)}")
    
    # Chunk examples
    number_chunks = numbers.chunk(2)
    print(f"   Numbers chunked by 2: {number_chunks}")
    string_chunks = strings.chunk(1)
    print(f"   Strings chunked by 1: {string_chunks}")
    
    # Dump_me example (commented out to avoid stopping execution)
    print(f"   Note: dump_me() method is available for debugging")
    print(f"   Example: numbers.dump_me() would stop execution and print collection details\n")
    
    # 4. All items operations
    print("4. All items operations:")
    all_numbers = numbers.all()
    all_strings = strings.all()
    all_empty = empty.all()
    
    print(f"   All numbers: {all_numbers}")
    print(f"   All strings: {all_strings}")
    print(f"   All empty: {all_empty}")
    
    # Demonstrate that all() returns a copy
    all_numbers.append(999)
    print(f"   Modified all_numbers: {all_numbers}")
    print(f"   Original numbers unchanged: {numbers}\n")
    
    # 5. Length operations
    print("5. Length operations:")
    print(f"   Numbers length: {len(numbers)}")
    print(f"   Strings length: {len(strings)}")
    print(f"   Empty length: {len(empty)}\n")
    
    # 6. Generic types demonstration
    print("6. Generic types demonstration:")
    
    # Typed collections
    int_collection: Collection[int] = Collection([10, 20, 30])
    str_collection: Collection[str] = Collection(["hello", "world"])
    list_collection: Collection[List[int]] = Collection([[1, 2], [3, 4]])
    
    print(f"   Int collection: {int_collection}")
    print(f"   String collection: {str_collection}")
    print(f"   List collection: {list_collection}")
    
    # Add items to typed collections
    int_collection.append(40)
    str_collection.append("python")
    list_collection.append([5, 6])
    
    print(f"   After append - Int: {int_collection}")
    print(f"   After append - String: {str_collection}")
    print(f"   After append - List: {list_collection}\n")
    
    # 7. Error handling demonstration
    print("7. Error handling demonstration:")
    
    # Try to get first/last from empty collection
    result = empty.first()
    print(f"   First from empty: {result}")
    
    try:
        result = empty.last()
        print(f"   Last from empty: {result}")
    except IndexError as e:
        print(f"   Error getting last from empty: {e}")
    
    # Clear the empty collection and try again
    empty = Collection()
    result = empty.first()
    print(f"   First from truly empty: {result}")
    
    # After method with no match
    print(f"   After non-existent element: {numbers.after(999)}")
    print(f"   After non-matching predicate: {numbers.after(lambda x: x > 100)}\n")
    
    # 8. String representation
    print("8. String representation:")
    print(f"   Numbers str(): {str(numbers)}")
    print(f"   Strings repr(): {repr(strings)}")
    print(f"   Empty str(): {str(empty)}")


if __name__ == "__main__":
    main()
