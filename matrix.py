from random import randint

class matrix():
    """
    Class that creates a matrix, list of lists, with x columns and y rows
    """
    def __init__(self, x, y):
        # refactor using nested list comprehension
        self.grid = [[randint(0, 9) for col_index in range(x)] for row_index in range (y)]
        '''
        self.grid = []
        for col_index in range(x):
            row = []
            for row_index in range(y):
                row.append(randint(0, 9))
            self.grid.append(row)
        '''

    def view_matrix(self):
        for row in self.grid:
            print(row)
        print('\n')

