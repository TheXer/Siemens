import pytest
from simpler_program import return_unique, foo1


@pytest.mark.parametrize(
    "items, expected_items",
    [
        ([1, 2, 3, 1, 1, 1, 1], [1, 2, 3]),
        (["hello world", "hello", "world", "hello"], ['hello', 'world', 'hello world']),
        ([1, "hello", 1, "hello"], [1, "hello"]),
    ]
)
def test_return_unique(items, expected_items):
    assert all([a == b for a, b in zip(return_unique(items), expected_items)])
