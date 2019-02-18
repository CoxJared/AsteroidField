class Bullet:
    verticies = (0, 0, 0), (0, .1, 0), (0, .1, .1), (0, 0, .1),\
            (.1, 0, 0), (.1, .1, 0), (.1, .1, .1), (.1, 0, .1)

    edges = (0, 1), (1, 2), (2, 3), (3, 0),\
            (4, 5), (5, 6), (6, 7), (7, 4),\
            (0, 4), (1, 5), (2, 6), (3, 7)

    def __init__(self, position = (0,0,0), rotation = (0,0)):

        self.x, self.y, self.z = position
        self.verticies = [(self.x+X/2, self.y+Y/2, self.z+Z/2) for X, Y, Z in self.verticies]
        self.rotation = list(rotation)
        self.destruct = self.x + 100