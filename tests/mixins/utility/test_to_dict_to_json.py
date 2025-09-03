import json

from src.py_collections.collection import Collection


class TestToDictToJson:
    def test_to_dict_primitives(self):
        c = Collection([1, 2.5, True, None, "x"])
        assert c.to_dict() == [1, 2.5, True, None, "x"]

    def test_to_dict_nested_containers(self):
        c = Collection([
            {"a": 1, "b": [1, 2, {"c": 3}]},
            (1, 2),
            {1: "one"},
            {"set": {1, 2}},
        ])

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

        items = Collection([
            dt.date(2020, 1, 2),
            dt.datetime(2020, 1, 2, 3, 4, 5),
            dt.time(3, 4, 5),
            dec.Decimal("1.23"),
            uuid.UUID("12345678-1234-5678-1234-567812345678"),
        ])

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

