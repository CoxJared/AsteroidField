import pygame
import math
import sys

import camera
import spaceShip
import asteroid
import random
import bullets

def getDistance(pos1, pos2):
    return math.sqrt( (pos1.x-pos2.x)**2+ (pos1.y-pos2.y)**2+(pos1.z-pos2.z)**2)

def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

def createRandomAsteroids(xrel, yrel, zrel, num = 150):
    asteroids = []
    for i in range(num):
        asteroids.append(addRandomAsteroid(xrel, yrel, zrel))
    return asteroids

def addRandomAsteroid(xrel, yrel, zrel ):
    
    xran = (xrel + 30, xrel + 100)
    yran = (yrel - 50, yrel + 50)
    zran = (zrel - 50, zrel + 50)

    x = random.randint(xran[0], xran[1])
    y = random.randint(yran[0], yran[1])
    z = random.randint(zran[0], zran[1])
    return asteroid.Asteroid((x, y, z),(1.672,1.6))

pygame.init()
w,h = 400, 400
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
cam = camera.Camera((0,0,-5))
pygame.event.get()

ship = spaceShip.Ship((0, 0, -8), (1.6, 1.6))

asteroids = createRandomAsteroids(0,0,-8)

bulletExists = False

running = True

print("a,d,w,s,q,e movement\nh,j,k,l rotation\n esc to exit")

while running:

    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    screen.fill((0,0,0))

    for edge in ship.edges:

        points = []
        for x, y, z in  (ship.verts[edge[0]], ship.verts[edge[1]]):

            x -= cam.x
            y -= cam.y
            z -= cam.z

            y, z = rotate2d((y, z), ship.rotation[1])
            x, z = rotate2d((x, z), ship.rotation[0])

            f = 200.0/z

            x, y = x*f, y*f
            points += [(cx + int(x), cy +int(y))]
        pygame.draw.line(screen, (102,255,102), points[0], points[1], 1)

    for ast in asteroids:
        if(ast.x  > (cam.x + 2 )):

            if(getDistance(ast,ship) < 1.5):
                running = False


            for edge in ast.edges:
                points = []
                for x, y, z in  (ast.verticies[edge[0]], ast.verticies[edge[1]]):

                    x -= cam.x
                    y -= cam.y
                    z -= cam.z

                    y, z = rotate2d((y,z ), ast.rotation[1])
                    x,z = rotate2d((x,z), ast.rotation[0])

                    try:
                        f = 200.0 / z
                    except:
                        print(z)
                    x, y = x*f, y*f
                    points += [(cx + int(x), cy +int(y))]

                ast.update(dt)
                if(points[0][0] > 0 and points[0][0] < w and points [0][1] > 0 and points[0][1] < h):
                    pygame.draw.line(screen, (255,153,255), points[0], points[1], 1)
                else:
                    try:
                        asteroids.remove(ast)
                        asteroids.append(addRandomAsteroid(int(ship.x), int(ship.y), int(ship.z)))
                    except:
                        pass
        else:
            asteroids.remove(ast)
            asteroids.append(addRandomAsteroid(int(ship.x), int(ship.y), int(ship.z)))


    key =pygame.key.get_pressed()

    #bullet Stuff
    if (key[pygame.K_SPACE] and not bulletExists):
        bulletExists = True
        bullet = bullets.Bullet((ship.x, ship.y, ship.z), ((1.6, 1.6)))

    if(bulletExists):
        for edge in bullet.edges:
            points = []
            for x, y, z in (bullet.verticies[edge[0]], bullet.verticies[edge[1]]):
                x -= cam.x
                y -= cam.y
                z -= cam.z

                y, z = rotate2d((y, z), bullet.rotation[1])
                x, z = rotate2d((x, z), bullet .rotation[0])
                if(z != 0):
                    f = 200 / z
                    x, y = x * f, y * f
                points += [(cx + int(x), cy + int(y))]

            pygame.draw.line(screen, (255, 255, 153), points[0], points[1], 1)
            bullet.update(dt)
        if(bullet.x > bullet.destruct):
            bulletExists = False

    ship.update(dt, key)
    cam.update(ship)

input("complete")
pygame.display.quit()
sys.exit()