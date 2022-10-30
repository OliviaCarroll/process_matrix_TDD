from random import randint

class Matrix():
    """
    Class that creates a matrix, list of lists, with x columns and y rows
    """
    def __init__(self, len_x, len_y):
        self.grid = [[randint(0, 9) for col_index in range(len_x)] for row_index in range (len_y)]
        self.num_rows = len_x
        self.num_columns = len_y

    def view_matrix(self):
        for row in self.grid:
            print(row)
        print('\n')
    
    def get_element_value(self, point):
        return self.grid[point.x][point.y]
