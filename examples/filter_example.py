#!/usr/bin/env python3
"""
Example demonstrating the Collection filter method.

This example shows how to use the filter method to create new collections
with elements that satisfy a predicate function.
"""

from py_collections import Collection


def main():
    print("=== Collection filter() Method Examples ===\n")
    
    # Example 1: Basic number filtering
    print("1. Basic number filtering:")
    numbers = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Original collection: {numbers}")
    
    # Filter even numbers
    even_numbers = numbers.filter(lambda x: x % 2 == 0)
    print(f"Even numbers: {even_numbers}")
    
    # Filter odd numbers
    odd_numbers = numbers.filter(lambda x: x % 2 == 1)
    print(f"Odd numbers: {odd_numbers}")
    
    # Filter numbers greater than 5
    greater_than_5 = numbers.filter(lambda x: x > 5)
    print(f"Numbers > 5: {greater_than_5}")
    print()
    
    # Example 2: String filtering
    print("2. String filtering:")
    fruits = Collection(["apple", "banana", "cherry", "date", "elderberry", "fig"])
    print(f"Original collection: {fruits}")
    
    # Filter fruits starting with 'a'
    a_fruits = fruits.filter(lambda s: s.startswith('a'))
    print(f"Fruits starting with 'a': {a_fruits}")
    
    # Filter fruits with length > 5
    long_fruits = fruits.filter(lambda s: len(s) > 5)
    print(f"Fruits with length > 5: {long_fruits}")
    
    # Filter fruits containing 'e'
    e_fruits = fruits.filter(lambda s: 'e' in s)
    print(f"Fruits containing 'e': {e_fruits}")
    print()
    
    # Example 3: Complex object filtering
    print("3. Complex object filtering:")
    class Person:
        def __init__(self, name: str, age: int, city: str):
            self.name = name
            self.age = age
            self.city = city
        
        def __repr__(self):
            return f"Person({self.name}, {self.age}, {self.city})"
    
    people = Collection([
        Person("Alice", 25, "New York"),
        Person("Bob", 30, "Los Angeles"),
        Person("Charlie", 35, "Chicago"),
        Person("David", 40, "Boston"),
        Person("Eve", 22, "Miami"),
        Person("Frank", 28, "Seattle")
    ])
    print(f"Original collection: {people}")
    
    # Filter people over 30
    over_30 = people.filter(lambda p: p.age > 30)
    print(f"People over 30: {over_30}")
    
    # Filter people with names starting with 'A'
    a_names = people.filter(lambda p: p.name.startswith('A'))
    print(f"People with names starting with 'A': {a_names}")
    
    # Filter people from specific cities
    east_coast = people.filter(lambda p: p.city in ["New York", "Boston"])
    print(f"East coast people: {east_coast}")
    print()
    
    # Example 4: Mixed type filtering
    print("4. Mixed type filtering:")
    mixed = Collection([1, "hello", 3.14, True, [1, 2, 3], None, False, "world"])
    print(f"Original collection: {mixed}")
    
    # Filter integers (excluding booleans)
    integers = mixed.filter(lambda x: isinstance(x, int) and not isinstance(x, bool))
    print(f"Integers: {integers}")
    
    # Filter strings
    strings = mixed.filter(lambda x: isinstance(x, str))
    print(f"Strings: {strings}")
    
    # Filter booleans
    booleans = mixed.filter(lambda x: isinstance(x, bool))
    print(f"Booleans: {booleans}")
    
    # Filter truthy values
    truthy = mixed.filter(lambda x: bool(x))
    print(f"Truthy values: {truthy}")
    print()
    
    # Example 5: Edge cases
    print("5. Edge cases:")
    
    # Empty collection
    empty_collection = Collection()
    filtered_empty = empty_collection.filter(lambda x: x > 0)
    print(f"Filtered empty collection: {filtered_empty}")
    
    # No matches
    no_matches = numbers.filter(lambda x: x > 100)
    print(f"No matches filter: {no_matches}")
    
    # All matches
    all_matches = numbers.filter(lambda x: x > 0)
    print(f"All matches filter: {all_matches}")
    print()
    
    # Example 6: Filter chaining
    print("6. Filter chaining:")
    collection = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Original collection: {collection}")
    
    # Chain multiple filters
    result = collection.filter(lambda x: x % 2 == 0)  # Even numbers
    print(f"After filtering even numbers: {result}")
    
    result = result.filter(lambda x: x > 5)  # Even numbers > 5
    print(f"After filtering > 5: {result}")
    
    result = result.filter(lambda x: x < 10)  # Even numbers 5 < x < 10
    print(f"Final result: {result}")
    print()
    
    # Example 7: Relationship with other methods
    print("7. Relationship with other methods:")
    collection = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # Get first even number
    first_even = collection.first(lambda x: x % 2 == 0)
    print(f"First even number: {first_even}")
    
    # Get all even numbers
    all_even = collection.filter(lambda x: x % 2 == 0)
    print(f"All even numbers: {all_even}")
    
    # Verify relationship
    print(f"First even equals first in filtered: {first_even == all_even.first()}")
    
    # Get element after first even
    after_first_even = collection.after(lambda x: x % 2 == 0)
    print(f"Element after first even: {after_first_even}")
    
    # Get all elements after even numbers
    after_even = all_even.filter(lambda x: collection.after(x) is not None)
    print(f"Even numbers that have a next element: {after_even}")


if __name__ == "__main__":
    main()
