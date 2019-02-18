import pygame
import math
import sys


def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

class Cam:
    def __init__(self, pos = (0,0,0), rot = (0,0)):
        self. pos = list(pos)
        self.rot = list(rot)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rot[0] += y
            self.rot[1] += x

    def update(self, dt, key):
        s = dt*10

        if(key[pygame.K_q]):
            self.pos[1] +=s
        if(key[pygame.K_e]):
            self.pos[1] -=s


        x, y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

        if key[pygame.K_w]:
           self.pos[0] += x
           self.pos[2] += y
        if key[pygame.K_s]:
            self.pos[0] -= x
            self.pos[2] -= y
        if key[pygame.K_d]:
            self.pos[0] -= y
            self.pos[2] += x
        if key[pygame.K_a]:
            self.pos[0] += y
            self.pos[2] -= x


        if(key[pygame.K_j]):
            self.rot[0] += s/3
        if(key[pygame.K_k]):
            self.rot[0] -= s/3
        if(key[pygame.K_l]):
            self.rot[1] +=s/3
        if(key[pygame.K_h]):
            self.rot[1] -=s/3

class Ship:
    verticies = (-3, -1, 1), ( -3, 1, 1), (-3, -1, -1), (-3, 1, -1), (3, -1, 1), (3, 1, 1), (3, -1, -1), (3, 1, -1), (-3, 0, 1), (3, 0, 1), (-4, 0, 2), (7, 0, 0), (-5, -3, 0), (-5, 3, 0)

    edges = (0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7), (0, 4), (1, 5), (2, 6), (3, 7), (8, 9), (8, 10), (9, 10), (4, 11), (5, 11), (6, 11), (7, 11), (0, 12), (2, 12), (4, 12), (6, 12), (1, 13), (3, 13), (5, 13), (7, 13)

    def __init__(self, pos = (0,0,0)):
        x, y, z = pos
        self.verts = [(x+X/2, y+Y/2, z+Z/2) for X, Y, Z in self.verticies]


pygame.init()
w,h = 400, 400
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
cam = Cam((0,0,-5))
pygame.event.get()
pygame.mouse.get_rel()
pygame.mouse.set_visible(0);
pygame.event.set_grab(1)

cubeCoords = (0, 0, 0) #(2, 2, 2), (2, 2, -2), (2, -2, -2), (-2, 2, -2), (2, -2, 2), (-2, -2, 2), (-2, -2, -2), (-2, 2, 2)'''

obj= Ship((0,0,0))# [Ship((x, y, z)) for x, y, z in cubeCoords]

while True:

    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((255,255,255))

    #for obj in objects:

    for edge in obj.edges:

        points = []
        for x, y, z in  (obj.verts[edge[0]], obj.verts[edge[1]]):

            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]

            x,z = rotate2d((x,z), cam.rot[1])
            y,z = rotate2d((y,z), cam.rot[0])


            f = 200/z
            x, y = x*f, y*f
            points += [(cx + int(x), cy +int(y))]
        pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)

    pygame.display.flip()

    key =pygame.key.get_pressed()
    cam.update(dt, key)

