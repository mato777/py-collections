#!/usr/bin/env python3
"""
Example demonstrating the group_by functionality of the Collection class.

This example shows how to use the group_by method to group collection items
by various criteria, similar to Laravel's Collection::groupBy method.
"""

from py_collections import Collection


def main():
    print("=== Collection group_by() Method Examples ===\n")
    
    # Example 1: Group by dictionary key
    print("1. Group by dictionary key:")
    users = Collection([
        {"name": "Alice", "department": "Engineering", "age": 25, "city": "NYC"},
        {"name": "Bob", "department": "Sales", "age": 30, "city": "LA"},
        {"name": "Charlie", "department": "Engineering", "age": 35, "city": "SF"},
        {"name": "Diana", "department": "Marketing", "age": 28, "city": "NYC"},
        {"name": "Eve", "department": "Engineering", "age": 32, "city": "LA"},
        {"name": "Frank", "department": "Sales", "age": 29, "city": "SF"}
    ])
    
    print(f"Users: {users}")
    
    # Group by department
    by_department = users.group_by("department")
    print(f"\nGrouped by department:")
    for dept, dept_users in by_department.items():
        names = [user["name"] for user in dept_users.all()]
        print(f"  {dept}: {names}")
    
    # Group by city
    by_city = users.group_by("city")
    print(f"\nGrouped by city:")
    for city, city_users in by_city.items():
        names = [user["name"] for user in city_users.all()]
        print(f"  {city}: {names}")
    print()
    
    # Example 2: Group by object attribute
    print("2. Group by object attribute:")
    class Product:
        def __init__(self, name: str, category: str, price: float):
            self.name = name
            self.category = category
            self.price = price
        
        def __repr__(self):
            return f"Product({self.name}, {self.category}, ${self.price})"
    
    products = Collection([
        Product("Laptop", "Electronics", 999.99),
        Product("Mouse", "Electronics", 29.99),
        Product("Book", "Books", 19.99),
        Product("Tablet", "Electronics", 499.99),
        Product("Notebook", "Books", 9.99),
        Product("Keyboard", "Electronics", 79.99)
    ])
    
    print(f"Products: {products}")
    
    # Group by category
    by_category = products.group_by("category")
    print(f"\nGrouped by category:")
    for category, category_products in by_category.items():
        names = [product.name for product in category_products.all()]
        print(f"  {category}: {names}")
    print()
    
    # Example 3: Group by callable function
    print("3. Group by callable function:")
    numbers = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    
    # Group by even/odd
    by_parity = numbers.group_by(lambda x: "even" if x % 2 == 0 else "odd")
    print(f"Numbers: {numbers}")
    print(f"Grouped by parity:")
    for parity, parity_numbers in by_parity.items():
        print(f"  {parity}: {parity_numbers.all()}")
    
    # Group by number range
    by_range = numbers.group_by(lambda x: f"{((x-1)//5)*5+1}-{((x-1)//5)*5+5}")
    print(f"\nGrouped by range:")
    for range_key, range_numbers in by_range.items():
        print(f"  {range_key}: {range_numbers.all()}")
    print()
    
    # Example 4: Group by age decade
    print("4. Group by age decade:")
    people = Collection([
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35},
        {"name": "Diana", "age": 28},
        {"name": "Eve", "age": 42},
        {"name": "Frank", "age": 19},
        {"name": "Grace", "age": 55},
        {"name": "Henry", "age": 33}
    ])
    
    # Group by age decade
    by_decade = people.group_by(lambda person: f"{(person['age'] // 10) * 10}s")
    print(f"People: {people}")
    print(f"Grouped by age decade:")
    for decade, decade_people in by_decade.items():
        names = [person["name"] for person in decade_people.all()]
        print(f"  {decade}: {names}")
    print()
    
    # Example 5: Group by item itself
    print("5. Group by item itself:")
    words = Collection(["apple", "banana", "apple", "cherry", "banana", "date", "cherry"])
    
    # Group identical items together
    by_word = words.group_by()
    print(f"Words: {words}")
    print(f"Grouped by word:")
    for word, word_group in by_word.items():
        print(f"  '{word}': {word_group.all()}")
    print()
    
    # Example 6: Group by multiple criteria
    print("6. Group by multiple criteria:")
    students = Collection([
        {"name": "Alice", "grade": "A", "subject": "Math"},
        {"name": "Bob", "grade": "B", "subject": "Math"},
        {"name": "Charlie", "grade": "A", "subject": "Science"},
        {"name": "Diana", "grade": "B", "subject": "Science"},
        {"name": "Eve", "grade": "A", "subject": "Math"},
        {"name": "Frank", "grade": "C", "subject": "Science"}
    ])
    
    # Group by grade and subject combination
    by_grade_subject = students.group_by(lambda student: (student["grade"], student["subject"]))
    print(f"Students: {students}")
    print(f"Grouped by grade and subject:")
    for (grade, subject), grade_subject_students in by_grade_subject.items():
        names = [student["name"] for student in grade_subject_students.all()]
        print(f"  Grade {grade} in {subject}: {names}")
    print()
    
    # Example 7: Working with grouped collections
    print("7. Working with grouped collections:")
    orders = Collection([
        {"id": 1, "customer": "Alice", "amount": 100, "status": "completed"},
        {"id": 2, "customer": "Bob", "amount": 150, "status": "pending"},
        {"id": 3, "customer": "Alice", "amount": 200, "status": "completed"},
        {"id": 4, "customer": "Charlie", "amount": 75, "status": "cancelled"},
        {"id": 5, "customer": "Bob", "amount": 300, "status": "completed"}
    ])
    
    # Group by customer and then analyze each group
    by_customer = orders.group_by("customer")
    print(f"Orders: {orders}")
    print(f"Analysis by customer:")
    
    for customer, customer_orders in by_customer.items():
        total_amount = sum(order["amount"] for order in customer_orders.all())
        completed_orders = customer_orders.filter(lambda order: order["status"] == "completed")
        pending_orders = customer_orders.filter(lambda order: order["status"] == "pending")
        
        print(f"  {customer}:")
        print(f"    Total orders: {len(customer_orders)}")
        print(f"    Total amount: ${total_amount}")
        print(f"    Completed: {len(completed_orders)}")
        print(f"    Pending: {len(pending_orders)}")
    print()
    
    # Example 8: Edge cases
    print("8. Edge cases:")
    
    # Empty collection
    empty = Collection()
    empty_grouped = empty.group_by("key")
    print(f"Empty collection grouped: {empty_grouped}")
    
    # Missing keys
    users_with_missing = Collection([
        {"name": "Alice", "age": 25},
        {"name": "Bob"},  # Missing age
        {"name": "Charlie", "age": 30}
    ])
    
    by_age = users_with_missing.group_by("age")
    print(f"Users with missing age: {users_with_missing}")
    print(f"Grouped by age (None for missing):")
    for age, age_users in by_age.items():
        names = [user["name"] for user in age_users.all()]
        print(f"  {age}: {names}")
    print()
    
    print("=== Group By Examples Complete ===")


if __name__ == "__main__":
    main()
