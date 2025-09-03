#!/usr/bin/env python3
"""
Example demonstrating the exists() method of the Collection class.

This example shows how to use the exists() method to check if elements
exist in a collection based on various conditions.
"""

from py_collections import Collection


def main():
    print("=== Collection exists() Method Examples ===\n")
    
    # Example 1: Basic existence check
    print("1. Basic existence check:")
    empty_collection = Collection()
    numbers = Collection([1, 2, 3, 4, 5])
    
    print(f"   Empty collection exists: {empty_collection.exists()}")
    print(f"   Numbers collection exists: {numbers.exists()}")
    print()
    
    # Example 2: Checking for specific values
    print("2. Checking for specific values:")
    fruits = Collection(["apple", "banana", "cherry", "date"])
    
    print(f"   Fruits: {fruits}")
    print(f"   Contains 'apple': {fruits.exists(lambda x: x == 'apple')}")
    print(f"   Contains 'grape': {fruits.exists(lambda x: x == 'grape')}")
    print(f"   Contains fruit starting with 'b': {fruits.exists(lambda x: x.startswith('b'))}")
    print()
    
    # Example 3: Numeric conditions
    print("3. Numeric conditions:")
    scores = Collection([85, 92, 78, 96, 88, 91])
    
    print(f"   Scores: {scores}")
    print(f"   Has perfect score (100): {scores.exists(lambda x: x == 100)}")
    print(f"   Has score above 90: {scores.exists(lambda x: x > 90)}")
    print(f"   Has failing score (below 60): {scores.exists(lambda x: x < 60)}")
    print()
    
    # Example 4: Complex objects
    print("4. Complex objects:")
    
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
        
        def __str__(self):
            return f"{self.name} ({self.age}, {self.city})"
    
    people = Collection([
        Person("Alice", 25, "New York"),
        Person("Bob", 30, "Los Angeles"),
        Person("Charlie", 35, "Chicago"),
        Person("Diana", 28, "Boston")
    ])
    
    print(f"   People: {people}")
    print(f"   Has person named 'Bob': {people.exists(lambda p: p.name == 'Bob')}")
    print(f"   Has person over 30: {people.exists(lambda p: p.age > 30)}")
    print(f"   Has person from 'Miami': {people.exists(lambda p: p.city == 'Miami')}")
    print()
    
    # Example 5: Multiple conditions
    print("5. Multiple conditions:")
    products = Collection([
        {"name": "Laptop", "price": 999, "in_stock": True},
        {"name": "Mouse", "price": 25, "in_stock": False},
        {"name": "Keyboard", "price": 150, "in_stock": True},
        {"name": "Monitor", "price": 300, "in_stock": True}
    ])
    
    print(f"   Products: {products}")
    print(f"   Has expensive item (>$500): {products.exists(lambda p: p['price'] > 500)}")
    print(f"   Has out-of-stock item: {products.exists(lambda p: not p['in_stock'])}")
    print(f"   Has item under $50: {products.exists(lambda p: p['price'] < 50)}")
    print()
    
    # Example 6: Edge cases
    print("6. Edge cases:")
    mixed_collection = Collection([1, None, "hello", 0, False, ""])
    
    print(f"   Mixed collection: {mixed_collection}")
    print(f"   Has None values: {mixed_collection.exists(lambda x: x is None)}")
    print(f"   Has truthy values: {mixed_collection.exists(lambda x: bool(x))}")
    print(f"   Has falsy values: {mixed_collection.exists(lambda x: not bool(x))}")
    print()
    
    # Example 7: Performance demonstration
    print("7. Performance demonstration:")
    large_collection = Collection(list(range(10000)))
    
    # Check for first element (should be fast)
    print(f"   Large collection (10,000 elements)")
    print(f"   Has element 0: {large_collection.exists(lambda x: x == 0)}")
    print(f"   Has element 9999: {large_collection.exists(lambda x: x == 9999)}")
    print(f"   Has element 10000: {large_collection.exists(lambda x: x == 10000)}")
    print()
    
    print("=== Examples completed ===")


if __name__ == "__main__":
    main()
