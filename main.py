import pygame
import math
import camera
import spaceShip
import sys
import asteroid
import random

def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

def createRandomAsteroids(num =50 ,xran = (30,100), yran = (-20,20), zran = (-20,20)):
    asteroids = []
    for i in range(num):
        x = random.randint(xran[0],xran[1])
        y = random.randint(yran[0], yran[1])
        z = random.randint(zran[0], zran[1])
        asteroids.append(asteroid.Asteroid((x, y, z),(1.672,1.6)))
    return asteroids

pygame.init()
w,h = 500, 500
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
cam = camera.Camera((0,0,-5))
pygame.event.get()

ship = spaceShip.Ship((20, 0, -8), (1.672, 1.6))

asteroids = createRandomAsteroids()

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

            x -= cam.x
            y -= cam.y
            z -= cam.z

            y, z = rotate2d((y, z), ship.rotation[1])
            x, z = rotate2d((x, z), ship.rotation[0])

            f = 200/z
            x, y = x*f, y*f
            points += [(cx + int(x), cy +int(y))]
        pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)
    for asteroid in asteroids:
        if(asteroid.x  > (cam.x + 2 )):
            for edge in asteroid.edges:
                points = []
                for x, y, z in  (asteroid.verticies[edge[0]], asteroid.verticies[edge[1]]):

                    x -= cam.x
                    y -= cam.y
                    z -= cam.z

                    y, z = rotate2d((y,z ), asteroid.rotation[1])
                    x,z = rotate2d((x,z), asteroid.rotation[0])


                    f = 200/z
                    x, y = x*f, y*f
                    points += [(cx + int(x), cy +int(y))]


                pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)





    pygame.display.flip()
    #Debugging
    if (False):
        print("ship: " +str(ship.x) +" "+ str(ship.y) + " "+ str(ship.z) + " ")
        #print(ship.rotation)
        #print("ast: " + str(asteroid.x) + " " + str(asteroid.y) + " " + str(asteroid.z) + " ")


    key =pygame.key.get_pressed()
    ship.update(dt, key)
    cam.update(ship)

