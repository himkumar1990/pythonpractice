import pytest


@pytest.fixture
def start():
    return "a"


@pytest.fixture
def order(start):
    return [start]


def test_fixtureTree(order):
    order.append("b")
    assert order == ["a", "b", "c"]
