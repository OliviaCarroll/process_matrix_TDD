import pytest
from functools import reduce
from process_matrix import get_average
'''
def test_process_matrix():
    test_matrix = [[]] 
    pass
'''


def test_get_average():
    assert get_average([1, 1, 1]) == 1
    assert get_average([4, 3, 0, 9]) == 4

def test_get_average_passed_empty_list_throws_exception():
    with pytest.raises(ZeroDivisionError):
        assert get_average([])

'''
def test_get_neighbour_values():
'''