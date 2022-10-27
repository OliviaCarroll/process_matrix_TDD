from functools import reduce
from matrix import matrix

## en vez de devolver una matriz en condiciones normales y una cadena cuando la cosa se escacharra, 
## devuelve siempre una matriz, y si hay error, lanza una excepción.

## hay decicir una manera de representar cada punto, 
## look at tutoria jueves 27 around 1h30 in 
## use lists or tuples, define functions to access the first and second coordinates 

## perhaps create object? listen to around 1h50 into video, para las que vamos mas sueltas

def process_matrix(matrix) -> matrix:
    """"
    Receives a matrix of any size, processes each element, returns a processed matrix
    Each element in the new matrix will be the average of the elements' original value and the values of its immediate neighbours,
    i.e. not including diagonals
    """
    # creates variable to store the processed matrix
    processed_matrix = [[]]
    # for each row in the matrix
        # for each element in the row
            # process element
            
            # add to the new matrix in the correct position
    # return the new matrix TODO change to processed_matrix
    return matrix

def process_element(coordinate, matrix) -> float: # check it needs coordinate!
    """
    Receives a coordinate, and the original matrix,
    calculates the average of the element at the coodinate and its neighbours
    and returns the average
    """
    pass
    valid_coordinates = get_valid_neighbour_indices(coordinate, matrix)
    items = get_neighbour_values(valid_coordinates, matrix)
    average = get_average(items)
    return average
    
def get_valid_neighbour_indices(coordinate, matrix) -> list:
    pass

def get_neighbour_values(point, matrix) -> tuple:
    pass

def get_average(numbers) -> float:
    """
    Receives a list of numbers (values of the neighbours for each element in matrix)
    and returns their average/mean
    """
    return reduce(lambda accum, i: (accum + i), numbers, 0)/len(numbers)