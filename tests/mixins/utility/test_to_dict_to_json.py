import json

import pytest

from py_collections.collection import Collection


class TestToDictToJson:
    def test_to_dict_primitives(self):
        c = Collection([1, 2.5, True, None, "x"])
        assert c.to_dict() == [1, 2.5, True, None, "x"]

    def test_to_dict_nested_containers(self):
        c = Collection(
            [
                {"a": 1, "b": [1, 2, {"c": 3}]},
                (1, 2),
                {1: "one"},
                {"set": {1, 2}},
            ]
        )

        result_default = c.to_dict()
        assert isinstance(result_default[0], dict)
        assert result_default[0]["b"][2]["c"] == 3
        assert isinstance(result_default[1], list)
        # default mode keeps non-string keys as-is
        assert 1 in result_default[2]
        # sets become lists
        assert isinstance(result_default[3]["set"], list)

        result_json = c.to_dict(mode="json")
        # json mode stringifies keys
        assert "1" in result_json[2]
        # sets still lists
        assert isinstance(result_json[3]["set"], list)

    def test_to_dict_dataclass_and_object(self):
        from dataclasses import dataclass

        @dataclass
        class D:
            x: int
            y: str

        class P:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        c = Collection([D(1, "a"), P("bob", 30)])
        r = c.to_dict()
        assert r[0] == {"x": 1, "y": "a"}
        assert r[1] == {"name": "bob", "age": 30}

    def test_to_dict_collection_inside(self):
        inner = Collection([1, 2])
        outer = Collection([inner, 3])
        assert outer.to_dict() == [[1, 2], 3]

    def test_to_dict_json_special_types(self):
        import datetime as dt
        import decimal as dec
        import uuid

        items = Collection(
            [
                dt.date(2020, 1, 2),
                dt.datetime(2020, 1, 2, 3, 4, 5),
                dt.time(3, 4, 5),
                dec.Decimal("1.23"),
                uuid.UUID("12345678-1234-5678-1234-567812345678"),
            ]
        )

        data = items.to_dict(mode="json")
        assert data[0] == "2020-01-02"
        assert data[1].startswith("2020-01-02T03:04:05")
        assert data[2].startswith("03:04:05")
        assert data[3] == 1.23
        assert data[4] == "12345678-1234-5678-1234-567812345678"

    def test_to_json_roundtrip(self):
        c = Collection([{"a": 1}, {"b": {"c": [1, 2]}}])
        s = c.to_json()
        assert isinstance(s, str)
        loaded = json.loads(s)
        assert loaded == c.to_dict(mode="json")

    def test_pydantic_models_if_available(self):
        try:
            from pydantic import BaseModel  # type: ignore
        except Exception:
            return

        class User(BaseModel):
            id: int
            name: str

        c = Collection([User(id=1, name="Alice")])
        d = c.to_dict()
        assert d == [{"id": 1, "name": "Alice"}]

        dj = c.to_dict(mode="json")
        assert dj == [{"id": 1, "name": "Alice"}]

        js = c.to_json()
        assert json.loads(js) == dj

    def test_to_dict_circular_references(self):
        """Test circular reference handling."""
        # Create circular reference
        a = Collection([1, 2])
        b = Collection([3, 4])
        a.append(b)
        b.append(a)

        result = a.to_dict()
        # The circular reference should be detected and marked as "[Circular]"
        # The actual result shows the circular reference is detected at the deepest level
        assert result == [1, 2, [3, 4, [1, 2, "[Circular]"]]]

    def test_to_dict_json_mode_duplicate_keys(self):
        """Test duplicate key detection in JSON mode."""
        # Create a dict with keys that would become the same string
        data = Collection([{1: "one", "1": "one_string"}])

        with pytest.raises(
            ValueError, match="Duplicate key after JSON stringification"
        ):
            data.to_dict(mode="json")

    def test_to_dict_json_mode_special_key_types(self):
        """Test JSON mode with special key types."""
        import datetime as dt
        import decimal as dec
        import uuid

        # Test with various key types that need special handling
        data = Collection(
            [
                {
                    dt.date(2020, 1, 1): "date_key",
                    dt.datetime(2020, 1, 1, 12, 0, 0): "datetime_key",
                    dt.time(12, 0, 0): "time_key",
                    uuid.UUID("12345678-1234-5678-1234-567812345678"): "uuid_key",
                    dec.Decimal("1.23"): "decimal_key",
                    None: "null_key",
                    (1, 2): "tuple_key",  # Will be converted to string
                }
            ]
        )

        result = data.to_dict(mode="json")
        assert isinstance(result[0], dict)
        # Keys should be converted to strings
        assert "2020-01-01" in result[0]
        assert "2020-01-01T12:00:00" in result[0]
        assert "12:00:00" in result[0]
        assert "12345678-1234-5678-1234-567812345678" in result[0]
        assert "1.23" in result[0]
        assert "null" in result[0]
        assert "<tuple:(1, 2)>" in result[0]

    def test_to_dict_objects_with_to_dict_method(self):
        """Test objects that have a to_dict method."""

        class CustomObject:
            def __init__(self, value):
                self.value = value

            def to_dict(self):
                return {"custom_value": self.value}

        data = Collection([CustomObject("test")])
        result = data.to_dict()
        assert result == [{"custom_value": "test"}]

    def test_to_dict_objects_with_failing_to_dict_method(self):
        """Test objects with to_dict method that fails."""

        class FailingObject:
            def __init__(self, value):
                self.value = value

            def to_dict(self):
                raise ValueError("to_dict failed")

        data = Collection([FailingObject("test")])
        result = data.to_dict()
        # Should fall back to __dict__ representation
        assert result == [{"value": "test"}]

    def test_to_dict_pydantic_v1_dict_method(self):
        """Test Pydantic v1 models with dict() method."""
        try:
            from pydantic import BaseModel
        except ImportError:
            pytest.skip("Pydantic not available")

        # Create a mock Pydantic v1 model that has dict() method
        class MockPydanticV1:
            def __init__(self, value):
                self.value = value

            def dict(self):
                return {"pydantic_v1_value": self.value}

        data = Collection([MockPydanticV1("test")])
        result = data.to_dict()
        assert result == [{"pydantic_v1_value": "test"}]

    def test_to_dict_pydantic_v2_model_dump_with_mode_error(self):
        """Test Pydantic v2 model_dump with TypeError (older signature)."""
        try:
            from pydantic import BaseModel
        except ImportError:
            pytest.skip("Pydantic not available")

        # Create a mock that simulates older Pydantic v2 without mode parameter
        class MockPydanticV2Old:
            def __init__(self, value):
                self.value = value

            def model_dump(self, mode=None):
                if mode is not None:
                    raise TypeError("mode parameter not supported")
                return {"pydantic_v2_value": self.value}

        data = Collection([MockPydanticV2Old("test")])
        result = data.to_dict(mode="json")
        assert result == [{"pydantic_v2_value": "test"}]

    def test_to_dict_final_fallback_string_representation(self):
        """Test final fallback to string representation."""

        # Create an object that doesn't have __dict__ by using __slots__
        class NoDictObject:
            __slots__ = ["value"]

            def __init__(self, value):
                self.value = value

        data = Collection([NoDictObject("test")])
        result = data.to_dict()
        # Should fall back to string representation since it doesn't have __dict__
        assert isinstance(result[0], str)
        assert "NoDictObject" in result[0]

    def test_to_dict_hashable_check(self):
        """Test the is_hashable function with unhashable objects."""

        class UnhashableObject:
            __slots__ = ["value"]

            def __init__(self):
                self.value = "test"

            def __hash__(self):
                raise TypeError("unhashable type")

        # This should not crash and should handle the unhashable object
        data = Collection([UnhashableObject()])
        result = data.to_dict()
        assert len(result) == 1
        assert isinstance(result[0], str)  # Should fall back to string representation

    def test_to_dict_circular_reference_in_containers(self):
        """Test circular reference detection in built-in containers."""
        # Create circular reference in list
        a = [1, 2]
        b = [3, 4]
        a.append(b)
        b.append(a)

        data = Collection([a])
        result = data.to_dict()
        # Should detect circular reference and mark it
        assert result == [[1, 2, [3, 4, "[Circular]"]]]

    def test_to_dict_circular_reference_in_sets(self):
        """Test circular reference detection in sets."""
        # Note: sets can't contain mutable objects, so we'll test with a different approach
        # Create a list that references itself
        circular_list = [1, 2]
        circular_list.append(circular_list)

        data = Collection([circular_list])
        result = data.to_dict()
        # Should detect circular reference
        assert result == [[1, 2, "[Circular]"]]

    def test_to_dict_circular_reference_in_dicts(self):
        """Test circular reference detection in dictionaries."""
        # Create circular reference in dict
        a = {"key1": "value1"}
        b = {"key2": "value2"}
        a["circular"] = b
        b["circular"] = a

        data = Collection([a])
        result = data.to_dict()
        # Should detect circular reference
        assert result == [{"key1": "value1", "circular": {"key2": "value2", "circular": "[Circular]"}}]

    def test_to_dict_dataclass_without_circular_reference(self):
        """Test dataclass conversion without circular references."""
        from dataclasses import dataclass

        @dataclass
        class Node:
            value: int
            name: str

        node1 = Node(1, "first")
        node2 = Node(2, "second")

        data = Collection([node1, node2])
        result = data.to_dict()
        assert result == [{"value": 1, "name": "first"}, {"value": 2, "name": "second"}]

    def test_to_dict_pydantic_without_circular_reference(self):
        """Test Pydantic model conversion without circular references."""
        try:
            from pydantic import BaseModel
        except ImportError:
            pytest.skip("Pydantic not available")

        class Node(BaseModel):
            value: int
            name: str

        node1 = Node(value=1, name="first")
        node2 = Node(value=2, name="second")

        data = Collection([node1, node2])
        result = data.to_dict()
        assert result == [{"value": 1, "name": "first"}, {"value": 2, "name": "second"}]

    def test_to_dict_pydantic_v1_dict_method_exception_handling(self):
        """Test Pydantic v1 dict() method that raises exception."""
        try:
            from pydantic import BaseModel
        except ImportError:
            pytest.skip("Pydantic not available")

        # Create a mock that simulates Pydantic v1 dict() method that fails
        class FailingPydanticV1:
            def __init__(self, value):
                self.value = value

            def dict(self):
                raise ValueError("dict() method failed")

        data = Collection([FailingPydanticV1("test")])
        result = data.to_dict()
        # Should fall back to __dict__ representation
        assert result == [{"value": "test"}]

    def test_to_dict_objects_with_failing_to_dict_method_exception_handling(self):
        """Test objects with to_dict method that raises exception and falls back."""

        class FailingToDictObject:
            def __init__(self, value):
                self.value = value

            def to_dict(self):
                raise ValueError("to_dict method failed")

        data = Collection([FailingToDictObject("test")])
        result = data.to_dict()
        # Should fall back to __dict__ representation
        assert result == [{"value": "test"}]

    def test_to_dict_circular_reference_in_objects_with_dict(self):
        """Test circular reference detection in objects with __dict__."""

        class Node:
            def __init__(self, value):
                self.value = value
                self.next_node = None

        # Create circular reference
        node1 = Node(1)
        node2 = Node(2)
        node1.next_node = node2
        node2.next_node = node1

        data = Collection([node1])
        result = data.to_dict()
        # Should detect circular reference
        assert result == [{"value": 1, "next_node": {"value": 2, "next_node": "[Circular]"}}]

    def test_to_dict_edge_cases(self):
        """Test various edge cases for better coverage."""
        # Test with empty collection
        empty = Collection()
        assert empty.to_dict() == []

        # Test with None values
        data = Collection([None, {"key": None}])
        result = data.to_dict()
        assert result == [None, {"key": None}]

        # Test with complex nested structures
        complex_data = Collection([
            {
                "list": [1, 2, {"nested": "value"}],
                "tuple": (1, 2, 3),
                "set": {1, 2, 3},
                "dict": {"a": 1, "b": 2}
            }
        ])
        result = complex_data.to_dict()
        assert len(result) == 1
        assert isinstance(result[0], dict)
        assert "list" in result[0]
        assert "tuple" in result[0]
        assert "set" in result[0]
        assert "dict" in result[0]
