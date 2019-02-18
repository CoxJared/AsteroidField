class Asteroid:
    verticies = (0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1),\
            (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)

    edges = (0, 1), (1, 3), (3, 2), (2, 0),\
            (4, 5), (5, 7), (7, 6), (6, 4),\
            (0, 4), (1, 5), (2, 6), (3, 7)

    def __init__(self, position = (0,0,0)):
        x, y, z = position
        self.verticies = [(x+X/2, y+Y/2, z+Z/2) for X, Y, Z in self.verticies]


