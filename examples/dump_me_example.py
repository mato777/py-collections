#!/usr/bin/env python3
"""
Example demonstrating the dump_me() and dump_me_and_die() methods of the Collection class.

This example shows how to use both debugging methods to inspect collection contents.
"""

from py_collections import Collection


def main():
    print("=== Collection dump_me() and dump_me_and_die() Examples ===\n")
    
    # Example 1: Basic dump_me() usage
    print("1. Basic dump_me() usage (doesn't stop execution):")
    numbers = Collection([1, 2, 3, 4, 5])
    print("Before dump_me():")
    print(f"   Collection: {numbers}")
    print("   Length:", len(numbers))
    
    print("\nCalling dump_me():")
    numbers.dump_me()
    
    print("After dump_me() (execution continues):")
    print(f"   Collection: {numbers}")
    print("   Length:", len(numbers))
    print()
    
    # Example 2: dump_me() with different data types
    print("2. dump_me() with different data types:")
    mixed = Collection([42, "hello", 3.14, True, None, [1, 2, 3], {"key": "value"}])
    print("Mixed collection dump:")
    mixed.dump_me()
    print()
    
    # Example 3: dump_me() with empty collection
    print("3. dump_me() with empty collection:")
    empty = Collection()
    empty.dump_me()
    print()
    
    # Example 4: dump_me() with custom objects
    print("4. dump_me() with custom objects:")
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self):
            return f"{self.name}({self.age})"
    
    people = Collection([
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 35)
    ])
    
    people.dump_me()
    print()
    
    # Example 5: dump_me_and_die() usage
    print("5. dump_me_and_die() usage (stops execution):")
    test_collection = Collection(["apple", "banana", "cherry"])
    print("About to call dump_me_and_die()...")
    print("This will print the collection and then stop execution.")
    
    # Uncomment the next line to see dump_me_and_die() in action
    # test_collection.dump_me_and_die()
    
    print("(dump_me_and_die() call was commented out to allow this example to complete)")
    print()
    
    # Example 6: Practical debugging scenario
    print("6. Practical debugging scenario:")
    data = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # Simulate some processing
    filtered = data.filter(lambda x: x % 2 == 0)
    print("After filtering even numbers:")
    filtered.dump_me()
    
    # Continue processing
    doubled = Collection([x * 2 for x in filtered.all()])
    print("After doubling the filtered numbers:")
    doubled.dump_me()
    print()
    
    # Example 7: Comparison between methods
    print("7. Comparison between dump_me() and dump_me_and_die():")
    sample = Collection(["a", "b", "c"])
    
    print("Using dump_me() (continues execution):")
    sample.dump_me()
    print("Execution continued!")
    
    print("\nUsing dump_me_and_die() (would stop execution):")
    print("(commented out to allow example to complete)")
    # sample.dump_me_and_die()
    # print("This line would not execute if dump_me_and_die() was called")
    print()
    
    print("=== Examples completed ===")
    print("\nNote: dump_me_and_die() was commented out in examples to allow")
    print("the script to complete. Uncomment those lines to see the")
    print("SystemExit behavior in action.")


if __name__ == "__main__":
    main()
