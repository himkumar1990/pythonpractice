import pytest


@pytest.fixture
def first_fixture():
    return "a"


@pytest.fixture
def second_fixture():
    return 1


def test_combined_fixtures(first_fixture, second_fixture):
    new_list = [first_fixture, second_fixture]

    assert new_list == ["a", 1]