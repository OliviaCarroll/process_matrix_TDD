from process_matrix import get_average, get_neighbouring_points, get_neighbour_values, get_valid_neighbours, process_matrix
from Matrix import Matrix
from Point import Point

matrix1 = Matrix(4,3)
matrix1.view_matrix()

matrix2 = process_matrix(matrix1)
matrix2.view_matrix()
