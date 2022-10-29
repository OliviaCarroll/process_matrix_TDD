from process_matrix import get_average, get_neighbour_indices, get_neighbour_values, get_valid_neighbour_indices, process_matrix
from matrix import matrix, point

matrix1 = matrix(4, 3)
# print(matrix1.grid) ## why does this not print, it was the .grid!! any way to avoid this?
matrix1.view_matrix()
processed_matrix_1 = process_matrix(matrix1)
processed_matrix_1.view_matrix()

coord1 = point(0,0)
coord2 = point(1,0)
coord3 = point(0,1)
coord4 = point(1,1)
#all_indices3 = [point(0,1), point(-1,1), point(1,1), point(0,0), point(0,2)]
#all_indices4 = [point(1,1), point(0, 1),point(2,1), point(1, 0), point(1, 2)]
#print(coord1.coord)
#print(coord2.coord)
#print(coord3.coord)
print(get_neighbour_values([coord1, coord2, coord3], matrix1))
print(get_average(get_neighbour_values([coord1, coord2, coord3], matrix1)))

print(get_neighbour_indices(coord4))
print(get_neighbour_indices(coord3)) 
## print(get_valid_neighbour_indices([all_indices3], matrix1))
