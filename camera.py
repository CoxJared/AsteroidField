import pygame
import math

class Camera:
    def __init__(self, position = (0,0,0), rotation = (0,0)):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.rotation = list(rotation)

    def update(self, ship):
        #Delays tracking, shows the movement
        dx = ((self.x) - (ship.x - 6) ) / 5
        dy = ((self.y) - (ship.y - 0)) / 5
        dz = ((self.z) - (ship.z + 3)) / 5
        self.x -= dx
        self.y -= dy
        self.z -= dz



