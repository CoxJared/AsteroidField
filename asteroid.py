import pygame
import random
import math

class Asteroid:

    def __init__(self, position = (0,0,0), rotation = (0, 0, 0)):

        self. size = random.randint(2, 4)
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        c = random.randint(0, 2)

        self.verticies = (0,0,-self.size-c),(-self.size,-self.size,self.size),\
                         (-self.size,self.size,self.size),(self.size,self.size,self.size),\
                         (self.size,-self.size,self.size),\
                         (-self.size,-self.size,-self.size),(-self.size,self.size,-self.size),\
                         (self.size,self.size,-self.size),(self.size,-self.size,self.size),\
                         (-self.size-a,0,0),(self.size+a,0,0),(0,self.size+b,0),\
                         (0,-self.size-b,0),(0,0,self.size+c),(0,0,-self.size-c)


        self.edges = (1,2),(2,3),(3,4),(4,1),\
                     (5,6),(6,7),(7,8),(8,5),\
                     (9,1),(9,2),(9,5),(9,6),\
                     (10,4),(10,3),(10,8),(10,7),\
                     (11,2),(11,3),(11,6),(11,7),\
                     (12,1),(12,4),(12,5),(12,8),\
                     (13,1),(13,2),(13,3),(13,4),\
                     (0,5),(0,6),(0,7),(0,8)

        self.faces = (9,2,1),(9,2,6),(9,1,5),(9,5,6),\
                     (10,4,3),(10,3,7),(10,7,8),(10,8,4),\
                     (11,2,3),(11,3,7),(11,7,6),(11,6,2),\
                     (12,1,4),(12,4,8),(12,8,5),(12,5,1),\
                     (13,1,2),(13,2,3),(13,3,4),(13,4,1),\
                     (0,5,6),(0,6,7),(0,7,8),(0,8,5)

        self.colors = []
        self.colorsApparent = []

        for i in range(24):
            col = random.randint(100,220)
            self.colors.append((col,col,col))
            self.colorsApparent.append(((0,0,0)))

        self.x, self.y, self.z = position
        self.verticies = [(self.x + X/2, self.y + Y/2, self.z + Z/2) for X, Y, Z in self.verticies]
        self.rotation = list(rotation)
        self.velocities = []
        self.velocities.append((random.randint(-10,-5) / 50))
        for i in range(2):
            self.velocities.append(random.randint(-20,20) / 50)
        self.color = (255,153,255)

    def add(self, points, dt):
        return (points[0] + self.velocities[0] * dt,\
                points[1] + self.velocities[1] * dt,\
                points[2] + self.velocities[2] * dt)


    def update (self, dt,ship):
        self.verticies = [(self.add(coords, dt)) for coords in self.verticies]
        perc  =  1 - self.getDistance(self.x,self.y,self.z,ship.x,ship.y,ship.z)/300
        for i in range(24):
            if(perc < 0):
                self.colorsApparent[i] = (0,0,0)
            else:
                self.colorsApparent[i] = \
                    (int(self.colors[i][0] * perc),
                     int(self.colors[i][1] * perc),
                     int(self.colors[i][2] * perc))

    def getDistance(self,a, b, c, d, e, f):
        return math.sqrt( ((a-d)**2) + (b-e)**2) +((math.fabs(c-f) )**2)