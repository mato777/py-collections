#!/usr/bin/env python3
"""
Example demonstrating the Collection first_or_raise method.

This example shows how to use the first_or_raise method to get the first element
or raise an ItemNotFoundException when no element is found.
"""

from py_collections.collection import Collection, ItemNotFoundException


def main():
    print("=== Collection first_or_raise() Method Examples ===\n")
    
    # Example 1: Basic usage when element exists
    print("1. Basic usage when element exists:")
    collection = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {collection}")
    
    # Get first element
    first = collection.first_or_raise()
    print(f"First element: {first}")
    
    # Get first even number
    first_even = collection.first_or_raise(lambda x: x % 2 == 0)
    print(f"First even number: {first_even}")
    
    # Get first number > 3
    first_greater_than_3 = collection.first_or_raise(lambda x: x > 3)
    print(f"First number > 3: {first_greater_than_3}")
    print()
    
    # Example 2: String collection
    print("2. String collection:")
    fruits = Collection(["apple", "banana", "cherry", "date"])
    print(f"Collection: {fruits}")
    
    # Get first fruit starting with 'b'
    first_b = fruits.first_or_raise(lambda s: s.startswith('b'))
    print(f"First fruit starting with 'b': {first_b}")
    
    # Get first fruit with length > 5
    first_long = fruits.first_or_raise(lambda s: len(s) > 5)
    print(f"First fruit with length > 5: {first_long}")
    print()
    
    # Example 3: Complex objects
    print("3. Complex objects:")
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
    
    # Find first person over 25
    first_over_25 = people.first_or_raise(lambda p: p.age > 25)
    print(f"First person over 25: {first_over_25}")
    
    # Find first person with name starting with 'C'
    first_c_name = people.first_or_raise(lambda p: p.name.startswith('C'))
    print(f"First person with name starting with 'C': {first_c_name}")
    print()
    
    # Example 4: Exception handling
    print("4. Exception handling:")
    
    # Empty collection
    empty_collection = Collection()
    print(f"Empty collection: {empty_collection}")
    
    try:
        result = empty_collection.first_or_raise()
        print(f"Result: {result}")
    except ItemNotFoundException as e:
        print(f"Caught exception: {e}")
    
    # No matching element
    collection = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {collection}")
    
    try:
        result = collection.first_or_raise(lambda x: x > 100)
        print(f"Result: {result}")
    except ItemNotFoundException as e:
        print(f"Caught exception: {e}")
    
    try:
        result = collection.first_or_raise(lambda x: x < 0)
        print(f"Result: {result}")
    except ItemNotFoundException as e:
        print(f"Caught exception: {e}")
    print()
    
    # Example 5: Comparison with first() method
    print("5. Comparison with first() method:")
    collection = Collection([1, 2, 3, 4, 5])
    
    # When element exists, both methods return the same result
    first_result = collection.first(lambda x: x % 2 == 0)
    first_or_raise_result = collection.first_or_raise(lambda x: x % 2 == 0)
    
    print(f"first() result: {first_result}")
    print(f"first_or_raise() result: {first_or_raise_result}")
    print(f"Results are equal: {first_result == first_or_raise_result}")
    
    # When element doesn't exist, first() returns None, first_or_raise() raises exception
    print(f"first() with no match: {collection.first(lambda x: x > 100)}")
    
    try:
        collection.first_or_raise(lambda x: x > 100)
    except ItemNotFoundException as e:
        print(f"first_or_raise() with no match raises: {e}")
    print()
    
    # Example 6: Practical use case
    print("6. Practical use case:")
    
    # Simulate finding a user by ID
    class User:
        def __init__(self, id: int, name: str):
            self.id = id
            self.name = name
        
        def __repr__(self):
            return f"User({self.id}, {self.name})"
    
    users = Collection([
        User(1, "Alice"),
        User(2, "Bob"),
        User(3, "Charlie")
    ])
    
    # Find user with ID 2
    try:
        user = users.first_or_raise(lambda u: u.id == 2)
        print(f"Found user: {user}")
    except ItemNotFoundException:
        print("User not found")
    
    # Try to find non-existent user
    try:
        user = users.first_or_raise(lambda u: u.id == 999)
        print(f"Found user: {user}")
    except ItemNotFoundException:
        print("User not found")
    
    # Example 7: Error handling patterns
    print("\n7. Error handling patterns:")
    
    def find_user_by_id(users_collection, user_id):
        """Helper function to find user by ID with proper error handling."""
        try:
            return users_collection.first_or_raise(lambda u: u.id == user_id)
        except ItemNotFoundException:
            print(f"User with ID {user_id} not found")
            return None
    
    # Test the helper function
    user = find_user_by_id(users, 1)
    if user:
        print(f"Found user: {user}")
    
    user = find_user_by_id(users, 999)
    if user:
        print(f"Found user: {user}")


if __name__ == "__main__":
    main()
