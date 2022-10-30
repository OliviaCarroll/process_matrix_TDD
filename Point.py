class Point():
    """
    Class that creates coordinates as lists
    """
    def __init__(self, x, y):
        self.coord = [x, y]
        self.x = x
        self.y = y

    def print_point(self):
        print(self.coord)