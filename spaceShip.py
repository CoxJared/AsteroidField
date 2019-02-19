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
        self.verts = [(self.x+X, self.y+Y, self.z+Z) for X, Y, Z in self.verticies]
        self.rotation = list(rotation)
        self.rotationCorrection = 0
        self.rollRight= False
        self.rollLeft = False
        self.radsLeft = 0

    def update(self, dt, key):
        s = dt*7

        self.x += s * 3

        if (key[pygame.K_a]):
            self.y += s * 2
            self.rotation[1] -= s / 5
            self.rotationCorrection -= s / 5

        if (key[pygame.K_d]):
            self.y -= s * 2
            self.rotation[1] += s / 5
            self.rotationCorrection += s / 5


        # z-direct
        if key[pygame.K_s]:
            self.z -= s * 2
        if key[pygame.K_w]:
            self.z += s * 2

        if key[pygame.K_h] and (self.rotation[1]% (2*math.pi))<2.2:
            self.rotation[1] += s / 3
        if key[pygame.K_l] and (self.rotation[1]% (2*math.pi))> 0.7:
            self.rotation[1] -= s / 3

        if key[pygame.K_j] and not self.rollLeft:
            self.rollLeft = True
            self.radsLeft = math.pi * 2
        if key[pygame.K_k] and not self.rollRight:
            self.rollRight = True
            self.radsLeft = math.pi * 2


        if self.rollLeft:
            if self.radsLeft > .6 :
                self.y += s * 7
                self.z += s*3
                self.rotation[1] -= .6
                self.radsLeft -= .6
            else:
                self.rotation[1] -= self.radsLeft
                self.radsLeft = 0
                self.y -= s * 7
                self.z -= s * 5
                self.rollLeft = False
        if self.rollRight:
            if self.radsLeft > .6 :
                self.y -= s * 7
                self.z += s*3
                self.rotation[1] += .6
                self.radsLeft -= .6
            else:
                self.rotation[1] += self.radsLeft
                self.radsLeft = 0
                self.y += s * 7
                self.z -= s * 5
                self.rollRight = False


        if(self.rotationCorrection != 0):
            fix = self.rotationCorrection / 2
            self.rotation[1] -= fix
            self.rotationCorrection -= fix


        self.verts = [(self.x + X / 2, self.y + Y / 2, self.z + Z / 2) for X, Y, Z in self.verticies]



