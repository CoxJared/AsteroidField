import pygame
import math
import camera
import spaceShip
import sys
import asteroid

def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

pygame.init()
w,h = 500, 500
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
cam = camera.Camera((0,0,-5))
pygame.event.get()

ship = spaceShip.Ship((6.7, -.25, -7.8), (1.672, 1.6))

asteroid = asteroid.Asteroid((16.1, 1.6, -7.8))

print("a,d,w,s,q,e movement\nh,j,k,l rotation\n esc to exit")

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

    for edge in ship.edges:

        points = []
        for x, y, z in  (ship.verts[edge[0]], ship.verts[edge[1]]):

            x -= cam.position[0]
            y -= cam.position[1]
            z -= cam.position[2]

            y, z = rotate2d((y, z), ship.rotation[1])
            x, z = rotate2d((x, z), ship.rotation[0])

            f = 200/z
            x, y = x*f, y*f
            points += [(cx + int(x), cy +int(y))]
        pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)

    for edge in asteroid.edges:

        points = []
        for x, y, z in  (ship.verticies[edge[0]], ship.verticies[edge[1]]):

            x -= cam.position[0]
            y -= cam.position[1]
            z -= cam.position[2]

            x,y = rotate2d((x,y ), cam.rotation[1])
            x,z = rotate2d((x,z), cam.rotation[0])


            f = 200/z
            x, y = x*f, y*f
            points += [(cx + int(x), cy +int(y))]
        pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)





    pygame.display.flip()
    #Debugging
    if (False):
        print(str(ship.x) +" "+ str(ship.y) + " "+ str(ship.z) + " ")
        print(ship.rotation)


    key =pygame.key.get_pressed()
    ship.update(dt, key)

