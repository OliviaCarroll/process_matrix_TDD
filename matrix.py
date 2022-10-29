from random import randint

class matrix():
    """
    Class that creates a matrix, list of lists, with x columns and y rows
    """
    def __init__(self, len_x, len_y):
        # refactor using list comprehension
        self.grid = [[randint(0, 9) for col_index in range(len_x)] for row_index in range (len_y)]
        self.num_columns = len_x
        self.num_rows = len_y

    def view_matrix(self):
        for row in self.grid:
            print(row)
        print('\n')
    
    def get_element_value(self, point):
        return self.grid[point.x][point.y]

class point():
    """
    Class that creates coordinates as lists
    """
    def __init__(self, x, y):
        self.coord = [x, y]
        self.x = x
        self.y = y
'''
    def get_neighbours_indices(self):
        # create a list of points with x values between 0 and 
        all_indices = []
        all_indices.append(self.coord)
        if self.x >= 0 and self.x < 
'''     


'''
        self.grid = []
        for col_index in range(y):
            row = []
            for row_index in range(x):
                row.append(randint(0, 9))
            self.grid.append(row)
'''