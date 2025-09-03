#!/usr/bin/env python3
"""
Example demonstrating Collection with generic types.
"""

from typing import List
from py_collections import Collection


def main():
    """Demonstrate Collection generic type functionality."""
    
    print("=== Collection Generic Type Examples ===\n")
    
    # Int collection
    print("1. Int collection:")
    int_collection: Collection[int] = Collection([1, 2, 3])
    int_collection.append(4)
    print(f"   Int collection: {int_collection}")
    print(f"   First int: {int_collection.first()} (type: {type(int_collection.first()).__name__})")
    print(f"   Last int: {int_collection.last()} (type: {type(int_collection.last()).__name__})\n")
    
    # String collection
    print("2. String collection:")
    str_collection: Collection[str] = Collection(["apple", "banana"])
    str_collection.append("cherry")
    print(f"   String collection: {str_collection}")
    print(f"   First string: {str_collection.first()} (type: {type(str_collection.first()).__name__})")
    print(f"   Last string: {str_collection.last()} (type: {type(str_collection.last()).__name__})\n")
    
    # List collection
    print("3. List collection:")
    list_collection: Collection[List[int]] = Collection([[1, 2], [3, 4]])
    list_collection.append([5, 6])
    print(f"   List collection: {list_collection}")
    print(f"   First list: {list_collection.first()} (type: {type(list_collection.first()).__name__})")
    print(f"   Last list: {list_collection.last()} (type: {type(list_collection.last()).__name__})\n")
    
    # Custom class collection
    print("4. Custom class collection:")
    
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
        
        def __str__(self):
            return f"Person({self.name}, {self.age})"
    
    person_collection: Collection[Person] = Collection([
        Person("Alice", 25),
        Person("Bob", 30)
    ])
    person_collection.append(Person("Charlie", 35))
    print(f"   Person collection: {person_collection}")
    first_person = person_collection.first()
    last_person = person_collection.last()
    print(f"   First person: {first_person.name}, age {first_person.age}")
    print(f"   Last person: {last_person.name}, age {last_person.age}")
    print(f"   Person type: {type(first_person).__name__}\n")
    
    # Mixed types (without type annotation)
    print("5. Mixed types (without type annotation):")
    mixed_collection = Collection([42, "string", [1, 2, 3], {"key": "value"}])
    print(f"   Mixed collection: {mixed_collection}")
    print(f"   Types: {[type(item).__name__ for item in mixed_collection.all()]}")


if __name__ == "__main__":
    main()
