#!/usr/bin/env python3
"""
Script to run all Collection examples sequentially.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_example(example_file: str):
    """Run a single example file."""
    print(f"\n{'='*60}")
    print(f"Running: {example_file}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([sys.executable, example_file], 
                              capture_output=True, text=True, cwd=Path(__file__).parent)
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error running {example_file}:")
            print(result.stderr)
            
    except Exception as e:
        print(f"Failed to run {example_file}: {e}")


def main():
    """Run all example files."""
    examples_dir = Path(__file__).parent
    
    # List of example files to run (in order)
    example_files = [
        "init_example.py",
        "append_example.py", 
        "first_last_example.py",
        "first_with_predicate_example.py",
        "all_example.py",
        "generic_types_example.py",
        "edge_cases_example.py",
        "comprehensive_example.py",
        "typed_collections.py"
    ]
    
    print("Running all Collection examples...")
    print(f"Examples directory: {examples_dir}")
    
    for example_file in example_files:
        file_path = examples_dir / example_file
        if file_path.exists():
            run_example(example_file)
        else:
            print(f"Warning: {example_file} not found")
    
    print(f"\n{'='*60}")
    print("All examples completed!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
