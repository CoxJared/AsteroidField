import pygame
import math

class Camera:
    def __init__(self, position = (0,0,0), rotation = (0,0)):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.rotation = list(rotation)

    def update(self, ship):
        dx = ((self.x) - (ship.x - 6) ) / 10
        dy = ((self.y) - (ship.y - 0)) / 10
        dz = ((self.z) - (ship.z + 3)) / 10
        self.x -= dx
        self.y -= dy
        self.z -= dz



