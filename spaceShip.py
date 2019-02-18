import pygame
import math

class Ship:
    '''
    Coords:
        4: back points
        4: front points
        3: top wing
        1: front tip
        2: tip wings
    '''
    verticies = \
            (-3, -1, 1), ( -3, 1, 1), (-3, -1, -1), (-3, 1, -1), \
            (3, -1, 1), (3, 1, 1), (3, -1, -1), (3, 1, -1), \
            (-3, 0, 1), (3, 0, 1), (-4, 0, 2), \
            (7, 0, 0), \
            (-5, -3, 0), (-5, 3, 0)

    edges = (0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7), (0, 4), (1, 5), (2, 6), (3, 7), (8, 9), (8, 10), (9, 10), (4, 11), (5, 11), (6, 11), (7, 11), (0, 12), (2, 12), (4, 12), (6, 12), (1, 13), (3, 13), (5, 13), (7, 13)

    def __init__(self, position = (0,0,0), rotation = (0,0)):
        self.x, self.y, self.z = position
        self.verts = [(self.x+X/2, self.y+Y/2, self.z+Z/2) for X, Y, Z in self.verticies]
        self.rotation = list(rotation)

    def update(self, dt, key):
        s = dt*5

        #x-direct
        if key[pygame.K_w]:
            self.x += s
        if key[pygame.K_s]:
            self.x -= s

        # y-direct
        if (key[pygame.K_a]):
            self.y += s
        if (key[pygame.K_d]):
            self.y -= s
        # z-direct
        if key[pygame.K_q]:
            self.z -= s
        if key[pygame.K_e]:
            self.z += s

        if key[pygame.K_j]:
            self.rotation[0] += s/5
        if key[pygame.K_k]:
            self.rotation[0] -= s/5
        if key[pygame.K_h]:
            self.rotation[1] += s / 5
        if key[pygame.K_l]:
            self.rotation[1] -= s / 5

        self.verts = [(self.x + X / 2, self.y + Y / 2, self.z + Z / 2) for X, Y, Z in self.verticies]



