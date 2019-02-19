import pygame
import random

class Asteroid:

    def __init__(self, position = (0,0,0), rotation = (0, 0, 0)):

        size = random.randint(1, 3)
        a = random.randint(0, 10) / 10 * size
        b = random.randint(0, 10) / 10 * size
        c = random.randint(0, 10) / 10 * size

        self.verticies = (0, 0, 0), (0, a, 0), (0, b, a), (0, 0, c), \
                    (b, 0, 0), (c, b, 0), (b, a, c), (c, 0, a)

        self.edges = (0, 1), (1, 2), (2, 3), (3, 0), \
                (4, 5), (5, 6), (6, 7), (7, 4), \
                (0, 4), (1, 5), (2, 6), (3, 7)

        self.x, self.y, self.z = position
        self.verticies = [(self.x+X/2, self.y+Y/2, self.z+Z/2) for X, Y, Z in self.verticies]
        self.rotation = list(rotation)
        self.velocities = []
        self.velocities.append((random.randint(-10,-5) / 50))
        for i in range(2):
            self.velocities.append(random.randint(-10,10) / 50)

    def add(self, points, dt):
        return (points[0] + self.velocities[0] * dt,\
                points[1] + self.velocities[1] * dt,\
                points[2] + self.velocities[2] * dt)




    def update (self, dt):
        self.verticies = [(self.add(coords, dt)) for coords in self.verticies]

