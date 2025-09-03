#!/usr/bin/env python3
"""
Example demonstrating the dump_me method of the Collection class.

The dump_me method stops execution and prints all elements in the collection for debugging.
"""

from py_collections.collection import Collection


def main():
    print("=== Collection Dump Method Examples ===\n")
    
    # Example 1: Basic dump_me usage
    print("1. Basic dump_me usage:")
    print("Creating a collection and calling dump_me...")
    numbers = Collection([1, 2, 3, 4, 5])
    
    # This will stop execution and print the collection details
    print("About to call dump_me() - this will stop execution:")
    numbers.dump_me()
    
    # This line will never be reached due to SystemExit
    print("This line will never be reached!")


def demonstrate_dump_me_with_different_types():
    """Demonstrate dump_me with different data types."""
    print("\n=== Dump Examples with Different Types ===\n")
    
    # Example with strings
    print("String collection:")
    strings = Collection(['apple', 'banana', 'cherry'])
    strings.dump_me()
    
    # Example with mixed types
    print("Mixed types collection:")
    mixed = Collection([1, 'hello', 3.14, True, None])
    mixed.dump_me()
    
    # Example with complex objects
    print("Complex objects collection:")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self):
            return f"Person({self.name}, {self.age})"
    
    people = Collection([
        Person("Alice", 30),
        Person("Bob", 25),
        [1, 2, 3],
        {'key': 'value'}
    ])
    people.dump_me()


def demonstrate_debugging_scenario():
    """Demonstrate a realistic debugging scenario."""
    print("\n=== Debugging Scenario ===\n")
    
    # Simulate a scenario where you're debugging data processing
    data = Collection([10, 20, 30, 40, 50])
    
    # Process some data
    processed = data.filter(lambda x: x > 25)
    
    print("Original data processed. Now let's debug the filtered collection:")
    print("Calling dump_me() to inspect the filtered collection...")
    
    # Debug the filtered collection
    processed.dump_me()


if __name__ == "__main__":
    # Uncomment one of these to see the dump_me method in action:
    
    # Basic example
    main()
    
    # Different types example
    # demonstrate_dump_me_with_different_types()
    
    # Debugging scenario example
    # demonstrate_debugging_scenario()
