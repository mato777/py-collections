#!/usr/bin/env python3
"""
Example demonstrating the chunk method of the Collection class.

The chunk method splits a collection into smaller collections of the specified size.
"""

from py_collections import Collection


def main():
    print("=== Collection Chunk Method Examples ===\n")
    
    # Example 1: Basic chunking
    print("1. Basic chunking with size 3:")
    numbers = Collection([1, 2, 3, 4, 5, 6, 7, 8, 9])
    chunks = numbers.chunk(3)
    print(f"Original: {numbers}")
    print(f"Chunks: {chunks}")
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i + 1}: {chunk}")
    print()
    
    # Example 2: Chunking with size larger than collection
    print("2. Chunking with size larger than collection:")
    small_collection = Collection([1, 2, 3])
    large_chunks = small_collection.chunk(5)
    print(f"Original: {small_collection}")
    print(f"Chunks: {large_chunks}")
    for i, chunk in enumerate(large_chunks):
        print(f"  Chunk {i + 1}: {chunk}")
    print()
    
    # Example 3: Chunking with size 1
    print("3. Chunking with size 1 (individual elements):")
    words = Collection(['apple', 'banana', 'cherry', 'date'])
    single_chunks = words.chunk(1)
    print(f"Original: {words}")
    print(f"Chunks: {single_chunks}")
    for i, chunk in enumerate(single_chunks):
        print(f"  Chunk {i + 1}: {chunk}")
    print()
    
    # Example 4: Chunking with mixed types
    print("4. Chunking with mixed types:")
    mixed = Collection([1, 'hello', 3.14, True, None, 'world'])
    mixed_chunks = mixed.chunk(2)
    print(f"Original: {mixed}")
    print(f"Chunks: {mixed_chunks}")
    for i, chunk in enumerate(mixed_chunks):
        print(f"  Chunk {i + 1}: {chunk}")
    print()
    
    # Example 5: Empty collection
    print("5. Chunking empty collection:")
    empty = Collection()
    empty_chunks = empty.chunk(3)
    print(f"Original: {empty}")
    print(f"Chunks: {empty_chunks}")
    print()
    
    # Example 6: Error handling
    print("6. Error handling examples:")
    try:
        numbers.chunk(0)  # This should raise ValueError
    except ValueError as e:
        print(f"Error with size 0: {e}")
    
    try:
        numbers.chunk(-1)  # This should raise ValueError
    except ValueError as e:
        print(f"Error with negative size: {e}")
    
    try:
        numbers.chunk(2.5)  # This should raise ValueError
    except ValueError as e:
        print(f"Error with float size: {e}")
    print()
    
    # Example 7: Practical use case - processing data in batches
    print("7. Practical use case - processing data in batches:")
    data = Collection([f"item_{i}" for i in range(1, 11)])
    batch_size = 3
    batches = data.chunk(batch_size)
    
    print(f"Processing {len(data)} items in batches of {batch_size}:")
    for batch_num, batch in enumerate(batches, 1):
        print(f"  Processing batch {batch_num}: {batch}")
        # Simulate processing each batch
        for item in batch.all():
            print(f"    Processing: {item}")
        print(f"  Batch {batch_num} complete!")
        print()


if __name__ == "__main__":
    main()
