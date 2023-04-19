import pytest

from mafia_allocation import Allocator


@pytest.mark.parametrize("random_list", [(["1", "2"],), ([str(i) for i in range(11)])])
def test_allocator_raises_value_error(random_list):
    with pytest.raises(ValueError):
        Allocator(random_list, "test")


def test_ot_get_allocation_once(allocator):
    assert type(allocator.get_allocation_once()) == list
    assert allocator.get_allocation_once() != allocator.get_allocation_once()


def test_ot_get_allocation_for_all_games(allocator):
    result = allocator.get_allocation_for_all_games(2)
    assert type(result) == dict
    assert result[1] != result[2]
