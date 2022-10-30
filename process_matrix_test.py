import pytest
from process_matrix import get_average, get_neighbour_values, get_valid_neighbour_indices

def test_get_average():
    assert get_average([1, 1, 1]) == 1
    assert get_average([4, 3, 0, 9]) == 4
    assert get_average([3]) == 3

def test_get_average_passed_empty_list_throws_exception():
    with pytest.raises(ZeroDivisionError):
        assert get_average([])

'''
## Look in to mocking to pass randomness in as dependency...
def test_get_neighbour_values():
    test_matrix1 = [[1, 1, 1],
                    [2, 1 ,1],
                    [1, 1, 1]]
    test_matrix3 = [[1],
                    [3]]
    test_matrix4 = [[1,2,3]]


    assert get_neighbour_values([[0,0],[0,1],[1,0]], test_matrix1) == [1, 1, 2]
    assert get_neighbour_values([[1,1],[0,1],[2,1],[1,0],[1,2]], test_matrix1) == [1,1,1,2,1]
    assert get_neighbour_values([[0,0],[1,0]], test_matrix3) == [1,3]
    assert get_neighbour_values([[0,1],[0,0],[0,2]], test_matrix4) == [2,1,3]

def test_get_valid_neighbour_indices():
    test_grid0 = [[0,0]]
    test_matrix1 = [[1, 1, 1],
                    [2, 1 ,1],
                    [1, 1, 1]]
    test_matrix3 = [[1],
                    [3]]
    test_matrix4 = [[1,2,3]]

    assert get_valid_neighbour_indices([0,0], test_grid0) == [[0,0]]
    assert get_valid_neighbour_indices([0,0], test_matrix1) == [[0,0],[0,1],[1,0]]
    assert get_valid_neighbour_indices([1,1], test_matrix1) == [[0,0],[0,1],[1,0]]

'''