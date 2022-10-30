from functools import reduce
from Matrix import Matrix
from Point import Point

def process_matrix(matrix: Matrix) -> Matrix:
    """
    Receives matrix, processes it if of type Matrix
    """
    if is_numerical_matrix(matrix):
        return _process_matrix(matrix)
    else:
        raise TypeError('Only numerical matrices can be processed') 


def _process_matrix(matrix) -> Matrix:
    """"
    Receives a matrix of any size, processes each element, returns a new matrix
    Each element in the new matrix will be the average of the elements' original value and the values of its immediate neighbours,
    i.e. not including diagonals
    """
    new_grid = []
    # for each row in the matrix grid
    for x, row in enumerate(matrix.grid):
        # for each element in the row of the grid
        new_row = []
        for y, value in enumerate(row):            
            # process element
            point = Point(x, y)
            processed_point = process_element(point, matrix)
            new_row.append(processed_point)
        new_grid.append(new_row)    
    matrix.grid = new_grid
    return matrix

def is_numerical_matrix(matrix) -> bool:
    """
    Checks that the argument passed to process_matrix is an instance of Matrix
    """
    return type(matrix) == Matrix

def process_element(point: Point, matrix: Matrix) -> float:
    """
    Receives a coordinate, and the original matrix,
    calculates the average of the element at the coodinate and its neighbours
    and returns the average
    """
    neighbours = get_neighbouring_points(point)
    valid_neighbours = get_valid_neighbours(neighbours, matrix)
    neighbour_values = get_neighbour_values(valid_neighbours, matrix)
    average_of_neighbours = get_average(neighbour_values)
    return average_of_neighbours

def get_neighbouring_points(point: Point) -> list: 
    """
    Receives a point and returns a list of its neighbours, including the point itself
    """
    all_points = []

    for x in range(point.x-1, point.x+2):
        for y in range(point.y-1, point.y+2):
            if is_self(point, x, y):
                all_points.append(Point(x, y))
                continue
            if not is_diagonal_coord(point, x, y):
                all_points.append(Point(x,y))
    return all_points

def is_diagonal_coord(point: Point, x: int, y: int) -> bool:
    x_difference = x - point.x
    y_difference = y - point.y
    return x_difference == y_difference or x_difference + y_difference == 0

def is_self(point: Point, x: int, y: int) -> bool:
    return point.x == x and point.y == y

def get_valid_neighbours(indices: list, matrix: Matrix) -> list:
    """
    Receives a coordinate and the matrix, validates that coordinates exist on grid 
    returns a list of valid neighbour coordinates 
    """
    valid_points = []
    for point in indices:
        if point.x >= 0 and point.x < matrix.num_columns:
            if point.y >= 0 and point.y < matrix.num_rows:
                valid_points.append(point)
    return valid_points

def get_neighbour_values(indices: list, matrix: Matrix) -> list:
    """
    Receives a list of coordinates (of a position and its neighbouring elements) and a matrix,
    returns a list of the associated values
    """
    all_values = []
    for point in indices:
            value = matrix.get_element_value(point)
            all_values.append(value)
    return all_values

def get_average(numbers: list) -> float:
    """
    Receives a list of numbers
    and returns their average/mean rounded to 2 decimal places
    """
    return round(reduce(lambda accum, i: (accum + i), numbers, 0)/len(numbers), 2)