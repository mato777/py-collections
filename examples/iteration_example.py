#!/usr/bin/env python3
"""
Example demonstrating iteration functionality of the Collection class.

This example shows how to use Collection objects in for loops and with
various Python built-in functions that work with iterables.
"""

from py_collections import Collection


def main():
    print("=== Collection Iteration Examples ===\n")
    
    # Basic iteration
    print("1. Basic iteration:")
    numbers = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {numbers}")
    print("Iterating through items:")
    for item in numbers:
        print(f"  - {item}")
    print()
    
    # Iteration with different data types
    print("2. Iteration with different data types:")
    mixed = Collection(["hello", 42, True, [1, 2, 3], {"key": "value"}])
    print(f"Collection: {mixed}")
    print("Iterating through items:")
    for i, item in enumerate(mixed):
        print(f"  [{i}]: {item} (type: {type(item).__name__})")
    print()
    
    # List comprehension
    print("3. List comprehension:")
    numbers = Collection([1, 2, 3, 4, 5])
    print(f"Original: {numbers}")
    
    # Double each number
    doubled = [item * 2 for item in numbers]
    print(f"Doubled: {doubled}")
    
    # Filter even numbers
    evens = [item for item in numbers if item % 2 == 0]
    print(f"Even numbers: {evens}")
    print()
    
    # Built-in functions with iteration
    print("4. Built-in functions with iteration:")
    numbers = Collection([1, 2, 3, 4, 5])
    print(f"Collection: {numbers}")
    
    # Sum
    total = sum(item for item in numbers)
    print(f"Sum: {total}")
    
    # Max and min
    max_val = max(item for item in numbers)
    min_val = min(item for item in numbers)
    print(f"Max: {max_val}, Min: {min_val}")
    
    # Any and all
    has_even = any(item % 2 == 0 for item in numbers)
    all_positive = all(item > 0 for item in numbers)
    print(f"Has even numbers: {has_even}")
    print(f"All positive: {all_positive}")
    print()
    
    # Iteration after modifications
    print("5. Iteration after modifications:")
    collection = Collection([1, 2, 3])
    print(f"Initial: {collection}")
    
    collection.append(4)
    collection.append(5)
    print(f"After appending: {collection}")
    
    print("Iterating through modified collection:")
    for item in collection:
        print(f"  - {item}")
    print()
    
    # Empty collection iteration
    print("6. Empty collection iteration:")
    empty = Collection()
    print(f"Empty collection: {empty}")
    
    print("Iterating through empty collection:")
    count = 0
    for item in empty:
        count += 1
        print(f"  - {item}")
    
    print(f"Items found: {count}")
    print()
    
    # Complex iteration example
    print("7. Complex iteration example:")
    students = Collection([
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78},
        {"name": "Diana", "grade": 95}
    ])
    
    print("Student grades:")
    for student in students:
        print(f"  {student['name']}: {student['grade']}")
    
    # Calculate average grade
    total_grade = sum(student['grade'] for student in students)
    avg_grade = total_grade / len(students)
    print(f"Average grade: {avg_grade:.1f}")
    
    # Find students with grades above 90
    high_achievers = [student['name'] for student in students if student['grade'] > 90]
    print(f"High achievers (>90): {high_achievers}")
    print()
    
    print("=== Iteration Examples Complete ===")


if __name__ == "__main__":
    main()
