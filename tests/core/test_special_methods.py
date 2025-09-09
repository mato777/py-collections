"""Tests for Collection special methods (__eq__, __add__, __getitem__, etc.)."""

import pytest

from py_collections import Collection


class TestCollectionSpecialMethods:
    """Test cases for Collection special methods."""

    def test_eq_same_collections(self):
        """Test __eq__ with identical collections."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([1, 2, 3])
        assert collection1 == collection2

    def test_eq_different_items(self):
        """Test __eq__ with different items."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([1, 2, 4])
        assert collection1 != collection2

    def test_eq_different_order(self):
        """Test __eq__ with same items in different order."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([3, 2, 1])
        assert collection1 != collection2

    def test_eq_different_lengths(self):
        """Test __eq__ with collections of different lengths."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([1, 2])
        assert collection1 != collection2

    def test_eq_empty_collections(self):
        """Test __eq__ with empty collections."""
        collection1 = Collection([])
        collection2 = Collection([])
        assert collection1 == collection2

    def test_eq_with_none_collection(self):
        """Test __eq__ with None collection."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection(None)  # This creates an empty collection
        assert collection1 != collection2  # Non-empty != empty

    def test_eq_with_strings(self):
        """Test __eq__ with string collections."""
        collection1 = Collection(["hello", "world"])
        collection2 = Collection(["hello", "world"])
        collection3 = Collection(["hello", "python"])
        assert collection1 == collection2
        assert collection1 != collection3

    def test_eq_with_mixed_types(self):
        """Test __eq__ with mixed type collections."""
        collection1 = Collection([1, "hello", 3.14])
        collection2 = Collection([1, "hello", 3.14])
        collection3 = Collection([1, "world", 3.14])
        assert collection1 == collection2
        assert collection1 != collection3

    def test_eq_with_complex_objects(self):
        """Test __eq__ with complex objects."""

        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

            def __eq__(self, other):
                if not isinstance(other, Person):
                    return False
                return self.name == other.name and self.age == other.age

        person1 = Person("Alice", 30)
        person2 = Person("Bob", 25)
        person3 = Person("Alice", 30)

        collection1 = Collection([person1, person2])
        collection2 = Collection([person3, person2])
        collection3 = Collection([person1, person1])

        assert collection1 == collection2
        assert collection1 != collection3

    def test_eq_with_none_values(self):
        """Test __eq__ with None values."""
        collection1 = Collection([1, None, 3])
        collection2 = Collection([1, None, 3])
        collection3 = Collection([1, 2, 3])
        assert collection1 == collection2
        assert collection1 != collection3

    def test_eq_with_non_collection(self):
        """Test __eq__ with non-Collection objects."""
        collection = Collection([1, 2, 3])
        assert collection != [1, 2, 3]
        assert collection != "hello"
        assert collection != 42
        assert collection is not None

    def test_add_two_collections(self):
        """Test __add__ with two collections."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([4, 5, 6])
        result = collection1 + collection2
        expected = Collection([1, 2, 3, 4, 5, 6])
        assert result == expected

    def test_add_empty_collections(self):
        """Test __add__ with empty collections."""
        collection1 = Collection([])
        collection2 = Collection([])
        result = collection1 + collection2
        expected = Collection([])
        assert result == expected

    def test_add_one_empty_collection(self):
        """Test __add__ with one empty collection."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([])
        result1 = collection1 + collection2
        result2 = collection2 + collection1
        expected1 = Collection([1, 2, 3])
        expected2 = Collection([1, 2, 3])
        assert result1 == expected1
        assert result2 == expected2

    def test_add_with_strings(self):
        """Test __add__ with string collections."""
        collection1 = Collection(["hello"])
        collection2 = Collection(["world"])
        result = collection1 + collection2
        expected = Collection(["hello", "world"])
        assert result == expected

    def test_add_with_mixed_types(self):
        """Test __add__ with mixed type collections."""
        collection1 = Collection([1, "hello"])
        collection2 = Collection([3.14, True])
        result = collection1 + collection2
        expected = Collection([1, "hello", 3.14, True])
        assert result == expected

    def test_add_with_complex_objects(self):
        """Test __add__ with complex objects."""

        class Person:
            def __init__(self, name: str):
                self.name = name

            def __eq__(self, other):
                if not isinstance(other, Person):
                    return False
                return self.name == other.name

        person1 = Person("Alice")
        person2 = Person("Bob")
        collection1 = Collection([person1])
        collection2 = Collection([person2])
        result = collection1 + collection2
        expected = Collection([person1, person2])
        assert result == expected

    def test_add_with_none_values(self):
        """Test __add__ with None values."""
        collection1 = Collection([1, None])
        collection2 = Collection([None, 3])
        result = collection1 + collection2
        expected = Collection([1, None, None, 3])
        assert result == expected

    def test_add_returns_new_collection(self):
        """Test that __add__ returns a new Collection instance."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([4, 5, 6])
        result = collection1 + collection2
        assert result is not collection1
        assert result is not collection2
        assert isinstance(result, Collection)

    def test_add_preserves_original_collections(self):
        """Test that __add__ doesn't modify original collections."""
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([4, 5, 6])
        original1 = collection1._items.copy()
        original2 = collection2._items.copy()
        collection1 + collection2
        assert collection1._items == original1
        assert collection2._items == original2

    def test_add_with_non_collection_raises_type_error(self):
        """Test that __add__ raises TypeError with non-Collection objects."""
        collection = Collection([1, 2, 3])
        with pytest.raises(TypeError, match="Can only add Collection to Collection"):
            collection + [4, 5, 6]
        with pytest.raises(TypeError, match="Can only add Collection to Collection"):
            collection + "hello"
        with pytest.raises(TypeError, match="Can only add Collection to Collection"):
            collection + 42
        with pytest.raises(TypeError, match="Can only add Collection to Collection"):
            collection + None

    def test_add_commutative_property(self):
        """Test that addition is not commutative (order matters)."""
        collection1 = Collection([1, 2])
        collection2 = Collection([3, 4])
        result1 = collection1 + collection2
        result2 = collection2 + collection1
        assert result1 != result2
        assert result1 == Collection([1, 2, 3, 4])
        assert result2 == Collection([3, 4, 1, 2])

    def test_add_associative_property(self):
        """Test that addition is associative."""
        collection1 = Collection([1])
        collection2 = Collection([2])
        collection3 = Collection([3])
        result1 = (collection1 + collection2) + collection3
        result2 = collection1 + (collection2 + collection3)
        assert result1 == result2
        assert result1 == Collection([1, 2, 3])

    def test_getitem_valid_index(self):
        """Test __getitem__ with valid indices."""
        collection = Collection([10, 20, 30, 40, 50])
        assert collection[0] == 10
        assert collection[1] == 20
        assert collection[2] == 30
        assert collection[3] == 40
        assert collection[4] == 50
        assert collection[-1] == 50
        assert collection[-2] == 40

    def test_getitem_invalid_index(self):
        """Test __getitem__ with invalid indices raises IndexError."""
        collection = Collection([1, 2, 3])
        with pytest.raises(IndexError):
            collection[3]
        with pytest.raises(IndexError):
            collection[-4]

    def test_getitem_empty_collection(self):
        """Test __getitem__ with empty collection raises IndexError."""
        collection = Collection([])
        with pytest.raises(IndexError):
            collection[0]
        with pytest.raises(IndexError):
            collection[-1]

    def test_getitem_with_different_types(self):
        """Test __getitem__ with different data types."""
        collection = Collection(["hello", 42, 3.14, True, None])
        assert collection[0] == "hello"
        assert collection[1] == 42
        assert collection[2] == 3.14
        assert collection[3] is True
        assert collection[4] is None

    def test_getitem_with_complex_objects(self):
        """Test __getitem__ with complex objects."""

        class Person:
            def __init__(self, name: str):
                self.name = name

        person1 = Person("Alice")
        person2 = Person("Bob")
        collection = Collection([person1, person2])
        assert collection[0] is person1
        assert collection[1] is person2
        assert collection[0].name == "Alice"
        assert collection[1].name == "Bob"

    def test_getitem_slice_supported(self):
        """Test that __getitem__ supports slicing."""
        collection = Collection([1, 2, 3, 4, 5])
        result = collection[1:3]
        assert result == [2, 3]  # Returns a list slice, not a Collection

    def test_hash_not_implemented(self):
        """Test that Collection is not hashable."""
        collection = Collection([1, 2, 3])
        with pytest.raises(TypeError, match="unhashable type"):
            hash(collection)

    def test_contains_basic(self):
        """Test __contains__ method."""
        collection = Collection([1, 2, 3, "hello"])
        assert 1 in collection
        assert 2 in collection
        assert 3 in collection
        assert "hello" in collection
        assert 4 not in collection
        assert "world" not in collection

    def test_contains_with_none(self):
        """Test __contains__ with None values."""
        collection = Collection([1, None, 3])
        assert None in collection
        assert 1 in collection
        assert 3 in collection
        assert 2 not in collection

    def test_contains_with_complex_objects(self):
        """Test __contains__ with complex objects."""

        class Person:
            def __init__(self, name: str):
                self.name = name

            def __eq__(self, other):
                if not isinstance(other, Person):
                    return False
                return self.name == other.name

        person1 = Person("Alice")
        person2 = Person("Bob")
        person3 = Person("Alice")  # Same name as person1
        collection = Collection([person1, person2])
        assert person1 in collection
        assert person2 in collection
        assert person3 in collection  # Should work due to __eq__ implementation
        assert Person("Charlie") not in collection

    def test_len_basic(self):
        """Test __len__ method."""
        assert len(Collection([])) == 0
        assert len(Collection([1])) == 1
        assert len(Collection([1, 2, 3])) == 3
        assert len(Collection([1, 2, 3, 4, 5])) == 5

    def test_len_with_different_types(self):
        """Test __len__ with different data types."""
        collection = Collection(["hello", 42, 3.14, True, None])
        assert len(collection) == 5

    def test_len_with_complex_objects(self):
        """Test __len__ with complex objects."""

        class Person:
            def __init__(self, name: str):
                self.name = name

        people = Collection([Person("Alice"), Person("Bob"), Person("Charlie")])
        assert len(people) == 3

    def test_iter_basic(self):
        """Test __iter__ method."""
        collection = Collection([1, 2, 3])
        items = list(collection)
        assert items == [1, 2, 3]

    def test_iter_empty_collection(self):
        """Test __iter__ with empty collection."""
        collection = Collection([])
        items = list(collection)
        assert items == []

    def test_iter_with_different_types(self):
        """Test __iter__ with different data types."""
        collection = Collection(["hello", 42, 3.14, True, None])
        items = list(collection)
        assert items == ["hello", 42, 3.14, True, None]

    def test_iter_multiple_times(self):
        """Test that __iter__ can be called multiple times."""
        collection = Collection([1, 2, 3])
        items1 = list(collection)
        items2 = list(collection)
        assert items1 == items2
        assert items1 == [1, 2, 3]

    def test_iter_preserves_order(self):
        """Test that __iter__ preserves the order of items."""
        collection = Collection([3, 1, 4, 1, 5])
        items = list(collection)
        assert items == [3, 1, 4, 1, 5]

    def test_str_repr_consistency(self):
        """Test that __str__ and __repr__ are consistent."""
        collection = Collection([1, 2, 3])
        str_repr = str(collection)
        repr_repr = repr(collection)
        assert str_repr == repr_repr
        assert "Collection" in str_repr
        assert "[1, 2, 3]" in str_repr

    def test_str_repr_empty_collection(self):
        """Test __str__ and __repr__ with empty collection."""
        collection = Collection([])
        str_repr = str(collection)
        repr_repr = repr(collection)
        assert str_repr == repr_repr
        assert "Collection" in str_repr
        assert "[]" in str_repr

    def test_str_repr_with_different_types(self):
        """Test __str__ and __repr__ with different data types."""
        collection = Collection(["hello", 42, 3.14, True, None])
        str_repr = str(collection)
        assert "Collection" in str_repr
        assert "hello" in str_repr
        assert "42" in str_repr
        assert "3.14" in str_repr
        assert "True" in str_repr
        assert "None" in str_repr
