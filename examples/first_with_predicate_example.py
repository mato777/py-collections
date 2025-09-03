#!/usr/bin/env python3
"""
Example demonstrating Collection first method with predicate functions.
"""

from py_collections import Collection


def main():
    """Demonstrate Collection first method with predicate functionality."""
    
    print("=== Collection First with Predicate Examples ===\n")
    
    # Basic first without predicate (original behavior)
    print("1. Basic first without predicate (original behavior):")
    numbers = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"   Collection: {numbers}")
    print(f"   First element: {numbers.first()}\n")
    
    # First with predicate - find first even number
    print("2. First with predicate - find first even number:")
    first_even = numbers.first(lambda x: x % 2 == 0)
    print(f"   First even number: {first_even}\n")
    
    # First with predicate - find first number greater than 5
    print("3. First with predicate - find first number greater than 5:")
    first_greater_than_5 = numbers.first(lambda x: x > 5)
    print(f"   First number > 5: {first_greater_than_5}\n")
    
    # First with predicate - find first number divisible by 3
    print("4. First with predicate - find first number divisible by 3:")
    first_divisible_by_3 = numbers.first(lambda x: x % 3 == 0)
    print(f"   First number divisible by 3: {first_divisible_by_3}\n")
    
    # String collection examples
    print("5. String collection examples:")
    words = Collection(["apple", "banana", "cherry", "date", "elderberry"])
    print(f"   Words: {words}")
    
    # Find first word starting with 'b'
    first_b_word = words.first(lambda word: word.startswith('b'))
    print(f"   First word starting with 'b': {first_b_word}")
    
    # Find first word with length > 5
    first_long_word = words.first(lambda word: len(word) > 5)
    print(f"   First word with length > 5: {first_long_word}")
    
    # Find first word containing 'e'
    first_with_e = words.first(lambda word: 'e' in word)
    print(f"   First word containing 'e': {first_with_e}\n")
    
    # Mixed type collection examples
    print("6. Mixed type collection examples:")
    mixed = Collection([1, "hello", 3.14, True, [1, 2, 3], {"key": "value"}])
    print(f"   Mixed collection: {mixed}")
    
    # Find first string
    first_string = mixed.first(lambda x: isinstance(x, str))
    print(f"   First string: {first_string}")
    
    # Find first number (int or float)
    first_number = mixed.first(lambda x: isinstance(x, (int, float)))
    print(f"   First number: {first_number}")
    
    # Find first list
    first_list = mixed.first(lambda x: isinstance(x, list))
    print(f"   First list: {first_list}\n")
    
    # Custom class examples
    print("7. Custom class examples:")
    
    class Person:
        def __init__(self, name: str, age: int, city: str):
            self.name = name
            self.age = age
            self.city = city
        
        def __str__(self):
            return f"Person({self.name}, {self.age}, {self.city})"
    
    people = Collection([
        Person("Alice", 25, "New York"),
        Person("Bob", 30, "San Francisco"),
        Person("Charlie", 35, "Chicago"),
        Person("Diana", 28, "Boston"),
        Person("Eve", 22, "Los Angeles")
    ])
    
    print(f"   People: {people}")
    
    # Find first person over 25
    first_over_25 = people.first(lambda person: person.age > 25)
    print(f"   First person over 25: {first_over_25}")
    
    # Find first person from New York
    first_ny_person = people.first(lambda person: person.city == "New York")
    print(f"   First person from New York: {first_ny_person}")
    
    # Find first person with name starting with 'C'
    first_c_name = people.first(lambda person: person.name.startswith('C'))
    print(f"   First person with name starting with 'C': {first_c_name}\n")
    
    # Error handling examples
    print("8. Error handling examples:")
    
    # Try to find first number > 100 (no such number exists)
    try:
        result = numbers.first(lambda x: x > 100)
        print(f"   First number > 100: {result}")
    except IndexError as e:
        print(f"   Error: {e}")
    
    # Try to find first word starting with 'z' (no such word exists)
    try:
        result = words.first(lambda word: word.startswith('z'))
        print(f"   First word starting with 'z': {result}")
    except IndexError as e:
        print(f"   Error: {e}")
    
    # Empty collection
    empty = Collection()
    try:
        result = empty.first(lambda x: x > 0)
        print(f"   First positive number in empty collection: {result}")
    except IndexError as e:
        print(f"   Error: {e}")


if __name__ == "__main__":
    main()
