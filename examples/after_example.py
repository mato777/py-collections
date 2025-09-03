#!/usr/bin/env python3
"""
Example demonstrating the Collection after method.

This example shows how to use the after method to find the element
that comes after a specific element or predicate match.
"""

from py_collections.collection import Collection


def main():
    print("=== Collection after() Method Examples ===\n")
    
    # Example 1: Finding element after a specific value
    print("1. Finding element after a specific value:")
    numbers = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {numbers}")
    print(f"Element after 2: {numbers.after(2)}")  # 3
    print(f"Element after 4: {numbers.after(4)}")  # 5
    print(f"Element after 5: {numbers.after(5)}")  # None (last element)
    print(f"Element after 10: {numbers.after(10)}")  # None (not found)
    print()
    
    # Example 2: Finding element after predicate match
    print("2. Finding element after predicate match:")
    numbers = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Collection: {numbers}")
    print(f"Element after first even number: {numbers.after(lambda x: x % 2 == 0)}")  # 3
    print(f"Element after first number > 5: {numbers.after(lambda x: x > 5)}")  # 7
    print(f"Element after first number divisible by 3: {numbers.after(lambda x: x % 3 == 0)}")  # 4
    print()
    
    # Example 3: Working with strings
    print("3. Working with strings:")
    fruits = Collection(["apple", "banana", "cherry", "date", "elderberry"])
    print(f"Collection: {fruits}")
    print(f"Element after 'banana': {fruits.after('banana')}")  # cherry
    print(f"Element after fruit starting with 'b': {fruits.after(lambda s: s.startswith('b'))}")  # cherry
    print(f"Element after fruit with length > 5: {fruits.after(lambda s: len(s) > 5)}")  # cherry
    print()
    
    # Example 4: Working with complex objects
    print("4. Working with complex objects:")
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person({self.name}, {self.age})"
    
    people = Collection([
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 35),
        Person("David", 40)
    ])
    print(f"Collection: {people}")
    
    # Find person after someone over 25
    result = people.after(lambda p: p.age > 25)
    print(f"Person after first person over 25: {result}")
    
    # Find person after someone with name starting with 'B'
    result = people.after(lambda p: p.name.startswith('B'))
    print(f"Person after first person with name starting with 'B': {result}")
    print()
    
    # Example 5: Edge cases
    print("5. Edge cases:")
    empty_collection = Collection()
    print(f"Empty collection after(1): {empty_collection.after(1)}")  # None
    
    single_item = Collection([42])
    print(f"Single item collection after(42): {single_item.after(42)}")  # None
    
    duplicates = Collection([1, 2, 2, 3, 2, 4])
    print(f"Collection with duplicates: {duplicates}")
    print(f"Element after first occurrence of 2: {duplicates.after(2)}")  # 2 (second occurrence)
    print()
    
    # Example 6: Relationship with first() method
    print("6. Relationship with first() method:")
    collection = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {collection}")
    
    first_even = collection.first(lambda x: x % 2 == 0)  # 2
    after_first_even = collection.after(lambda x: x % 2 == 0)  # 3
    
    print(f"First even number: {first_even}")
    print(f"Element after first even number: {after_first_even}")
    print(f"Element after {first_even}: {collection.after(first_even)}")  # Should be same as above
    print(f"Consistency check: {after_first_even == collection.after(first_even)}")


if __name__ == "__main__":
    main()
