#!/usr/bin/env python3
"""
Example demonstrating the before method of the Collection class.

The before method returns the element that comes before the first occurrence
of the target element or predicate match.
"""

from py_collections.collection import Collection


def main():
    print("=== Collection Before Method Examples ===\n")
    
    # Example 1: Basic before usage with elements
    print("1. Basic before usage with elements:")
    numbers = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {numbers}")
    
    print(f"Before 3: {numbers.before(3)}")
    print(f"Before 1: {numbers.before(1)}")  # First element, so None
    print(f"Before 5: {numbers.before(5)}")
    print(f"Before 10: {numbers.before(10)}")  # Not found, so None
    print()
    
    # Example 2: Before with strings
    print("2. Before with strings:")
    words = Collection(['apple', 'banana', 'cherry', 'date', 'elderberry'])
    print(f"Collection: {words}")
    
    print(f"Before 'cherry': {words.before('cherry')}")
    print(f"Before 'apple': {words.before('apple')}")  # First element
    print(f"Before 'elderberry': {words.before('elderberry')}")
    print()
    
    # Example 3: Before with predicates
    print("3. Before with predicates:")
    numbers = Collection([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Collection: {numbers}")
    
    print(f"Before first even number: {numbers.before(lambda x: x % 2 == 0)}")
    print(f"Before first number > 5: {numbers.before(lambda x: x > 5)}")
    print(f"Before first number > 10: {numbers.before(lambda x: x > 10)}")  # No match
    print()
    
    # Example 4: Before with mixed types
    print("4. Before with mixed types:")
    mixed = Collection([1, 'hello', 3.14, True, None, 'world'])
    print(f"Collection: {mixed}")
    
    print(f"Before 3.14: {mixed.before(3.14)}")
    print(f"Before True: {mixed.before(True)}")
    print(f"Before None: {mixed.before(None)}")
    print()
    
    # Example 5: Before with duplicates
    print("5. Before with duplicates:")
    duplicates = Collection([1, 2, 3, 2, 4, 5, 2])
    print(f"Collection: {duplicates}")
    
    print(f"Before first occurrence of 2: {duplicates.before(2)}")
    print(f"Before first occurrence of 3: {duplicates.before(3)}")
    print()
    
    # Example 6: Edge cases
    print("6. Edge cases:")
    empty = Collection()
    single = Collection([42])
    two_elements = Collection([1, 2])
    
    print(f"Empty collection before 1: {empty.before(1)}")
    print(f"Single element before 42: {single.before(42)}")
    print(f"Two elements before 2: {two_elements.before(2)}")
    print(f"Two elements before 1: {two_elements.before(1)}")
    print()
    
    # Example 7: Practical use case - finding context
    print("7. Practical use case - finding context:")
    log_entries = Collection([
        'INFO: User login',
        'DEBUG: Processing request',
        'ERROR: Database connection failed',
        'INFO: User logout',
        'DEBUG: Cleanup completed'
    ])
    print(f"Log entries: {log_entries}")
    
    # Find the log entry before the first error
    before_error = log_entries.before(lambda entry: 'ERROR:' in entry)
    print(f"Log entry before first error: {before_error}")
    
    # Find the log entry before the first debug message
    before_debug = log_entries.before(lambda entry: 'DEBUG:' in entry)
    print(f"Log entry before first debug: {before_debug}")
    print()
    
    # Example 8: Comparison with after method
    print("8. Comparison with after method:")
    data = Collection([10, 20, 30, 40, 50])
    print(f"Collection: {data}")
    
    target = 30
    before_target = data.before(target)
    after_target = data.after(target)
    
    print(f"Target: {target}")
    print(f"Before target: {before_target}")
    print(f"After target: {after_target}")
    print(f"Before + Target + After: {before_target} -> {target} -> {after_target}")


if __name__ == "__main__":
    main()
