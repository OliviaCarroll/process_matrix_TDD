from process_matrix import get_neighbour_values, process_matrix
from matrix import matrix

matrix1 = matrix(4, 3)
# print(matrix1.grid) ## why does this not print, it was the .grid!! any way to avoid this?
matrix1.view_matrix()
processed_matrix_1 = process_matrix(matrix1)
processed_matrix_1.view_matrix()

print(get_neighbour_values([[0,0],[1,0],[0,1]], matrix1.grid))