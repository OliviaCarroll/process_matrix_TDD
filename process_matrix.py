from functools import reduce
from matrix import matrix, point

## en vez de devolver una matriz en condiciones normales y una cadena cuando la cosa se escacharra, 
## devuelve siempre una matriz, y si hay error, lanza una excepción.

'''
to get neighbour values, we have a list of coordinates or points and the original matrix
passed to the function 
cutre será una lista de dos elementos, es decir, punto = [2,3]
matriz = [[2,4],[5,6]]
puntos[[0,0],[0,1],[1,0]]
# to get each value
for coord in puntos:
    print("Value")
    print(matriz[coord[0]][coord[1]]) ## confusing
## could create two functions that get the x and y value from the point
def y_value(point): #first_coord
    return point[0]
def x_value(point): #second coord
    return point[1]
## so then getting the values is 
for point in puntos:
    print(matriz[y_value(point)][x_value(point)]) ## still not great
## create a function that gets the values in the background
def get_value(point, matrix):
    return matriz[y_value(point)][x_value(point)]
## iterate over the list of coordinates received
for point in points:
    print(get_value(point, matriz)) ## easier to read what is happening 
'''
'''
how to represent points
cuando estamos recorriendo la lista de puntos, ya nos olvidamos si es una lista tuple or whatever
solo importa que es un punto con sus funciones sencillitas 
get_first, get_second, get_value
así no hay que liarse con corchetes ni meter ceros para que sea una lista y luego quitar la cero
'''
## perhaps create object  
## try: class called points
## with methods for get x_coord, get y_coord, get_value


def process_matrix(matrix) -> matrix:
    """"
    Receives a matrix of any size, processes each element, returns a processed matrix
    Each element in the new matrix will be the average of the elements' original value and the values of its immediate neighbours,
    i.e. not including diagonals
    """
    if matrix == []:
        return matrix
    
    processed_matrix = [[]]

    # checks that what is passed in is correct, if not raise exception

    #else:
        # creates variable to store the processed matrix
        # for each row in the matrix
        # for each element in the row
            # process element
            
            # add to the new matrix in the correct position
        # return the new matrix TODO change to processed_matrix
    return matrix

def is_numerical_matrix(matrix) -> bool:
    """
    checks that matrix is a valid matrix
    """
    # matrix is a list of lists
    # the sublists are all the same size
    # the contents of each sublist is numbers only 
    pass

def process_element(coordinate, matrix) -> float: # check it needs coordinate
    """
    Receives a coordinate, and the original matrix,
    calculates the average of the element at the coodinate and its neighbours
    and returns the average
    """
    pass
    valid_coordinates = get_valid_neighbour_indices(coordinate, matrix)
    items = get_neighbour_values(valid_coordinates, matrix)
    average = round(get_average(items), 2)
    return average
    
def get_valid_neighbour_indices(indices: list, matrix) -> list:
    """
    Receives a coordinate and the matrix, validates that coordinates exist on grid 
    returns a list of valid neighbour coordinates 
    """
    valid_indices = []
    '''
    TODO find a way to filter the points...
    for point in indices:
        if point.x >= 0 and point.x < matrix.num_columns:
            if point.y >= 0 and point.y < matrix.num_rows:
                valid_indices.append(point)
    '''
    return valid_indices

def get_neighbour_indices(point): # returns a list of lists, TODO needs to return list of instances of point, how?
    #all_indices = []
    ## add original point to list of points 

    # all_indices.append(point(point.x, point.y))

    ## this works but creates list of lists
    '''
    all_indices.append(point1x = point(point.x-1, point.y))
    
    all_indices.append(point([point.x+1, point.y]))
    all_indices.append(point([point.x, point.y-1])) 
    all_indices.append(point([point.x, point.y+1]))
    '''
    ## need to create a list with instances of point in it to pass to get_valid_neighbour_indices
    return all_indices 

def get_neighbour_values(indices: list, matrix: matrix) -> list: #
    """
    Receives a list of coordinates (of a position and its neighbouring elements) and a matrix,
    returns a tuple of the associated values
    """
    all_values = []
    for point in indices:
        value = matrix.get_element_value(point)
        # value = grid[coordinate[0]][coordinate[1]] ##TODO refactor this
        all_values.append(value)
    return all_values

def get_average(numbers: list) -> float:
    """
    Receives a list of numbers
    and returns their average/mean
    """
    return reduce(lambda accum, i: (accum + i), numbers, 0)/len(numbers)