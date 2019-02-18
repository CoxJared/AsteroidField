import pygame
import math

class Camera:
    def __init__(self, position = (0,0,0), rotation = (0,0)):
        self. position = list(position)
        self.rotation = list(rotation)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rotation[0] += y
            self.rotation[1] += x


