#!/usr/bin/env python3
"""
Example demonstrating typed collections with proper type annotations.
This file shows how to use the Collection class with specific types.
"""

from typing import List, Dict, Optional
from py_collections import Collection, T


def demonstrate_int_collection():
    """Demonstrate Collection[int] usage."""
    print("=== Int Collection Example ===")
    
    # Type-annotated int collection
    numbers: Collection[int] = Collection([1, 2, 3, 4, 5])
    
    # Append more integers
    numbers.append(6)
    numbers.append(7)
    
    # Get the first and last numbers (type checker knows they're ints)
    first_number = numbers.first()
    last_number = numbers.last()
    print(f"First number: {first_number} (type: {type(first_number).__name__})")
    print(f"Last number: {last_number} (type: {type(last_number).__name__})")
    
    # Get all numbers using all() method
    all_numbers = numbers.all()
    print(f"All numbers: {all_numbers}")
    
    # Sum all numbers
    total = sum(all_numbers)
    print(f"Sum of all numbers: {total}")
    print()


def demonstrate_str_collection():
    """Demonstrate Collection[str] usage."""
    print("=== String Collection Example ===")
    
    # Type-annotated string collection
    words: Collection[str] = Collection(["hello", "world", "python"])
    
    # Append more strings
    words.append("collection")
    words.append("types")
    
    # Get the first and last words (type checker knows they're strs)
    first_word = words.first()
    last_word = words.last()
    print(f"First word: {first_word} (type: {type(first_word).__name__})")
    print(f"Last word: {last_word} (type: {type(last_word).__name__})")
    
    # Get all words using all() method
    all_words = words.all()
    print(f"All words: {all_words}")
    
    # Join all words
    sentence = " ".join(all_words)
    print(f"Complete sentence: {sentence}")
    print()


def demonstrate_list_collection():
    """Demonstrate Collection[List[int]] usage."""
    print("=== List Collection Example ===")
    
    # Type-annotated list collection
    matrix: Collection[List[int]] = Collection([[1, 2, 3], [4, 5, 6]])
    
    # Append more lists
    matrix.append([7, 8, 9])
    
    # Get the first row (type checker knows it's a List[int])
    first_row = matrix.first()
    print(f"First row: {first_row} (type: {type(first_row).__name__})")
    
    # Sum each row
    row_sums = [sum(row) for row in matrix.all()]
    print(f"Row sums: {row_sums}")
    print()


def demonstrate_dict_collection():
    """Demonstrate Collection[Dict] usage."""
    print("=== Dictionary Collection Example ===")
    
    # Type-annotated dict collection
    people: Collection[Dict[str, any]] = Collection([
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "San Francisco"}
    ])
    
    # Append more dictionaries
    people.append({"name": "Charlie", "age": 35, "city": "Chicago"})
    
    # Get the first person (type checker knows it's a Dict)
    first_person = people.first()
    print(f"First person: {first_person['name']} from {first_person['city']}")
    
    # Extract all names
    names = [person["name"] for person in people.all()]
    print(f"All names: {names}")
    print()


def demonstrate_custom_class_collection():
    """Demonstrate Collection[CustomClass] usage."""
    print("=== Custom Class Collection Example ===")
    
    class Product:
        def __init__(self, name: str, price: float, category: str):
            self.name = name
            self.price = price
            self.category = category
        
        def __str__(self):
            return f"{self.name} (${self.price:.2f})"
    
    # Type-annotated custom class collection
    products: Collection[Product] = Collection([
        Product("Laptop", 999.99, "Electronics"),
        Product("Book", 19.99, "Books"),
        Product("Coffee", 4.50, "Food")
    ])
    
    # Append more products
    products.append(Product("Headphones", 89.99, "Electronics"))
    
    # Get the first product (type checker knows it's a Product)
    first_product = products.first()
    print(f"First product: {first_product}")
    print(f"Category: {first_product.category}")
    
    # Calculate total value
    total_value = sum(product.price for product in products.all())
    print(f"Total value: ${total_value:.2f}")
    print()


def demonstrate_optional_collection():
    """Demonstrate Collection[Optional[T]] usage."""
    print("=== Optional Collection Example ===")
    
    # Type-annotated optional collection
    nullable_numbers: Collection[Optional[int]] = Collection([1, None, 3, None, 5])
    
    # Append more values
    nullable_numbers.append(7)
    nullable_numbers.append(None)
    
    # Get the first value (type checker knows it's Optional[int])
    first_value = nullable_numbers.first()
    print(f"First value: {first_value} (type: {type(first_value).__name__})")
    
    # Filter out None values
    valid_numbers = [num for num in nullable_numbers.all() if num is not None]
    print(f"Valid numbers: {valid_numbers}")
    print()


def demonstrate_generic_function():
    """Demonstrate generic function usage with Collection."""
    print("=== Generic Function Example ===")
    
    def process_collection(collection: Collection[T]) -> List[T]:
        """Generic function that works with any Collection type."""
        items = collection.all()
        # Double the collection size by duplicating items
        return items + items
    
    # Use with int collection
    int_coll: Collection[int] = Collection([1, 2, 3])
    doubled_ints = process_collection(int_coll)
    print(f"Doubled ints: {doubled_ints}")
    
    # Use with string collection
    str_coll: Collection[str] = Collection(["a", "b", "c"])
    doubled_strings = process_collection(str_coll)
    print(f"Doubled strings: {doubled_strings}")
    print()


def demonstrate_pydantic_collection():
    """Demonstrate Collection[PydanticModel] usage."""
    print("=== Pydantic Model Collection Example ===")
    
    try:
        from pydantic import BaseModel
        from typing import List as PydanticList
        
        class Product(BaseModel):
            id: int
            name: str
            price: float
            category: str
            in_stock: bool = True
        
        class Order(BaseModel):
            order_id: str
            customer_name: str
            products: PydanticList[Product]
            total_amount: float
        
        # Type-annotated Pydantic model collection
        products: Collection[Product] = Collection([
            Product(id=1, name="Laptop", price=999.99, category="Electronics"),
            Product(id=2, name="Book", price=19.99, category="Books", in_stock=False),
            Product(id=3, name="Coffee", price=4.50, category="Food")
        ])
        
        # Append more products
        products.append(Product(id=4, name="Headphones", price=89.99, category="Electronics"))
        
        # Get the first product (type checker knows it's a Product)
        first_product = products.first()
        print(f"First product: {first_product.name} (${first_product.price:.2f})")
        print(f"Category: {first_product.category}")
        print(f"In stock: {first_product.in_stock}")
        
        # Calculate total value
        total_value = sum(product.price for product in products.all())
        print(f"Total value: ${total_value:.2f}")
        
        # Create orders with products
        orders: Collection[Order] = Collection([
            Order(
                order_id="ORD-001",
                customer_name="Alice Johnson",
                products=[products.all()[0], products.all()[2]],
                total_amount=1004.49
            ),
            Order(
                order_id="ORD-002",
                customer_name="Bob Smith",
                products=[products.all()[3]],
                total_amount=89.99
            )
        ])
        
        # Get first order
        first_order = orders.first()
        print(f"\nFirst order: {first_order.order_id}")
        print(f"Customer: {first_order.customer_name}")
        print(f"Products: {len(first_order.products)} items")
        print(f"Total: ${first_order.total_amount:.2f}")
        
        # Serialize to JSON
        order_data = first_order.model_dump()
        print(f"Order data keys: {list(order_data.keys())}")
        
    except ImportError:
        print("Pydantic not available - skipping Pydantic example")
    print()


def main():
    """Run all demonstrations."""
    print("Typed Collections Demonstration\n")
    
    demonstrate_int_collection()
    demonstrate_str_collection()
    demonstrate_list_collection()
    demonstrate_dict_collection()
    demonstrate_custom_class_collection()
    demonstrate_optional_collection()
    demonstrate_generic_function()
    demonstrate_pydantic_collection()
    
    print("=== Type Safety Benefits ===")
    print("✓ Type checkers can verify correct types")
    print("✓ IDE provides better autocomplete")
    print("✓ Runtime type consistency")
    print("✓ Better code documentation")
    print("✓ Easier refactoring and maintenance")


if __name__ == "__main__":
    main()
