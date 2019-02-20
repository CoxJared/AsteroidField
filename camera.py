import pygame
import math

class Camera:
    def __init__(self, position = (0,0,0), rotation = (0,0)):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.rotation = list(rotation)

    def update1(self, ship):
        #Delays tracking, shows the movement
        dx = ((self.x) - (ship.x - 5) ) / 3
        dy = ((self.y) - (ship.y + 0)) / 3
        dz = ((self.z) - (ship.z +1)) / 3
        self.x -= dx
        self.y -= dy
        self.z -= dz


    def update2(self, dt, key):
        s = dt * 10

        if (key[pygame.K_q]):
            self.y += s
        if (key[pygame.K_e]):
            self.y -= s

        x, y = s * math.sin(self.rotation[1]), s * math.cos(self.rotation[1])

        if key[pygame.K_w]:
            self.x += x
            self.z += y
        if key[pygame.K_s]:
            self.x -= x
            self.z -= y
        if key[pygame.K_d]:
            self.x -= y
            self.z += x
        if key[pygame.K_a]:
            self.x += y
            self.z -= x

        if (key[pygame.K_j]):
            self.rotation[0] += s / 3
        if (key[pygame.K_k]):
            self.rotation[0] -= s / 3
        if (key[pygame.K_l]):
            self.rotation[1] += s / 3
        if (key[pygame.K_h]):
            self.rotation[1] -= s /3
