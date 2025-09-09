import pytest

from py_collections import Collection


class Dummy:
    def __init__(self, value):
        self.value = value


@pytest.mark.parametrize(
    "items,expected",
    [
        ([1, 2, 3, 4, 5], 3.0),
        ([10.0, 20.0, 30.0], 20.0),
        ([0, 0, 0], 0.0),
    ],
)
def test_average_basic(items, expected):
    c = Collection(items)
    assert c.average() == expected


@pytest.mark.parametrize(
    "items,key,expected",
    [
        ([{"price": 10}, {"price": 20}, {"price": 30}], "price", 20.0),
        ([{"a": 1}, {"a": 2}, {"a": 3}], "a", 2.0),
    ],
)
def test_average_key(items, key, expected):
    c = Collection(items)
    assert c.average(key) == expected


@pytest.mark.parametrize(
    "items,expected",
    [
        ([Dummy(2), Dummy(4), Dummy(6)], 4.0),
    ],
)
def test_average_attr(items, expected):
    c = Collection(items)
    assert c.average("value") == expected


@pytest.mark.parametrize(
    "items,func,expected",
    [
        (
            [{"price": 10}, {"price": 20}, {"price": 30}],
            lambda x: x["price"] * 1.1,
            22.0,
        ),
        ([1, 2, 3], lambda x: x * 2, 4.0),
    ],
)
def test_average_callback(items, func, expected):
    c = Collection(items)
    assert pytest.approx(c.average(func)) == expected


@pytest.mark.parametrize(
    "items",
    [
        ([]),
        (["a", "b", "c"]),
    ],
)
def test_average_empty_or_non_numeric(items):
    c = Collection(items)
    with pytest.raises(ValueError):
        c.average()


@pytest.mark.parametrize(
    "items,key",
    [
        ([{"a": "x"}, {"a": "y"}], "a"),
    ],
)
def test_average_key_non_numeric(items, key):
    c = Collection(items)
    with pytest.raises(TypeError):
        c.average(key)


@pytest.mark.parametrize(
    "items,key",
    [
        ([{"b": 1}], "a"),
    ],
)
def test_average_key_missing(items, key):
    c = Collection(items)
    with pytest.raises(KeyError):
        c.average(key)


@pytest.mark.parametrize(
    "items,func",
    [
        ([1, 2, 3], lambda x: str(x)),
    ],
)
def test_average_callback_non_numeric(items, func):
    c = Collection(items)
    with pytest.raises(TypeError):
        c.average(func)


def test_average_key_attribute_error():
    class NoAttr:
        pass

    c = Collection([NoAttr(), NoAttr()])
    with pytest.raises(AttributeError):
        c.average("missing_attr")


def test_average_key_no_values_found():
    c = Collection([])
    with pytest.raises(ValueError):
        c.average("any_key")


def test_average_callback_no_results():
    c = Collection([])
    with pytest.raises(ValueError):
        c.average(lambda x: x * 2)


def test_average_invalid_argument_type():
    c = Collection([1, 2, 3])
    with pytest.raises(TypeError):
        c.average(123)  # int is not allowed
    with pytest.raises(TypeError):
        c.average(["not", "allowed"])  # list is not allowed
    with pytest.raises(TypeError):
        c.average({"not": "allowed"})  # dict is not allowed
