import pytest
import sys
from io import StringIO
from src.py_collections.collection import Collection


class TestDumpMe:
    def test_dump_me_empty_collection(self):
        """Test dump_me with an empty collection."""
        collection = Collection()
        
        # Capture stdout to check the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            collection.dump_me()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        
        # Check that the output contains expected information
        assert "=== Collection Dump ===" in output
        assert "Collection: Collection([])" in output
        assert "Type: <class 'src.py_collections.collection.Collection'>" in output
        assert "Length: 0" in output
        assert "(empty collection)" in output
        assert "=== End Collection Dump ===" in output
    
    def test_dump_me_with_integers(self):
        """Test dump_me with a collection of integers."""
        collection = Collection([1, 2, 3, 4, 5])
        
        # Capture stdout to check the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            collection.dump_me()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        
        # Check that the output contains expected information
        assert "=== Collection Dump ===" in output
        assert "Collection: Collection([1, 2, 3, 4, 5])" in output
        assert "Type: <class 'src.py_collections.collection.Collection'>" in output
        assert "Length: 5" in output
        assert "[0]: 1 (type: int)" in output
        assert "[1]: 2 (type: int)" in output
        assert "[2]: 3 (type: int)" in output
        assert "[3]: 4 (type: int)" in output
        assert "[4]: 5 (type: int)" in output
        assert "=== End Collection Dump ===" in output
    
    def test_dump_me_with_strings(self):
        """Test dump_me with a collection of strings."""
        collection = Collection(['apple', 'banana', 'cherry'])
        
        # Capture stdout to check the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            collection.dump_me()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        
        # Check that the output contains expected information
        assert "=== Collection Dump ===" in output
        assert "Collection: Collection(['apple', 'banana', 'cherry'])" in output
        assert "Length: 3" in output
        assert "[0]: apple (type: str)" in output
        assert "[1]: banana (type: str)" in output
        assert "[2]: cherry (type: str)" in output
        assert "=== End Collection Dump ===" in output
    
    def test_dump_me_with_mixed_types(self):
        """Test dump_me with a collection of mixed types."""
        collection = Collection([1, 'hello', 3.14, True, None])
        
        # Capture stdout to check the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            collection.dump_me()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        
        # Check that the output contains expected information
        assert "=== Collection Dump ===" in output
        assert "Length: 5" in output
        assert "[0]: 1 (type: int)" in output
        assert "[1]: hello (type: str)" in output
        assert "[2]: 3.14 (type: float)" in output
        assert "[3]: True (type: bool)" in output
        assert "[4]: None (type: NoneType)" in output
        assert "=== End Collection Dump ===" in output
    
    def test_dump_me_with_complex_objects(self):
        """Test dump_me with a collection containing complex objects."""
        class TestObject:
            def __init__(self, value):
                self.value = value
            
            def __str__(self):
                return f"TestObject({self.value})"
        
        obj1 = TestObject("test1")
        obj2 = TestObject("test2")
        collection = Collection([obj1, obj2, [1, 2, 3], {'key': 'value'}])
        
        # Capture stdout to check the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            collection.dump_me()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        
        # Check that the output contains expected information
        assert "=== Collection Dump ===" in output
        assert "Length: 4" in output
        assert "[0]: TestObject(test1) (type: TestObject)" in output
        assert "[1]: TestObject(test2) (type: TestObject)" in output
        assert "[2]: [1, 2, 3] (type: list)" in output
        assert "[3]: {'key': 'value'} (type: dict)" in output
        assert "=== End Collection Dump ===" in output
    
    def test_dump_me_always_raises_system_exit(self):
        """Test that dump_me always raises SystemExit regardless of collection content."""
        # Test with empty collection
        empty_collection = Collection()
        with pytest.raises(SystemExit, match="Collection dump completed - execution stopped"):
            empty_collection.dump_me()
        
        # Test with non-empty collection
        non_empty_collection = Collection([1, 2, 3])
        with pytest.raises(SystemExit, match="Collection dump completed - execution stopped"):
            non_empty_collection.dump_me()
    
    def test_dump_me_output_format(self):
        """Test that dump_me output follows the expected format."""
        collection = Collection([42, "test"])
        
        # Capture stdout to check the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            collection.dump_me()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        
        # Check that the output has the expected structure
        lines = output.strip().split('\n')
        
        # Should have the header
        assert lines[0] == "=== Collection Dump ==="
        
        # Should have collection info
        assert any("Collection: Collection([42, 'test'])" in line for line in lines)
        assert any("Type: <class 'src.py_collections.collection.Collection'>" in line for line in lines)
        assert any("Length: 2" in line for line in lines)
        
        # Should have elements section
        assert any("Elements:" in line for line in lines)
        assert any("[0]: 42 (type: int)" in line for line in lines)
        assert any("[1]: test (type: str)" in line for line in lines)
        
        # Should have the footer
        assert lines[-1] == "=== End Collection Dump ==="
