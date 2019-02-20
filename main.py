import pygame
import math
import sys

import camera
import spaceShip
import asteroid
import random
import bullets

def getDistance(x1, y1, z1, x2, y2, z2):
    return math.sqrt( ((x1-x2)**2) + (y1-y2)**2) +((z1-z2)**2)

def rotate2d(x, y, rad):
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

def createRandomAsteroids(xrel, yrel, zrel, num = 50):
    asteroids = []
    for i in range(num):
        asteroids.append(addRandomAsteroid(xrel, yrel, zrel))
    return asteroids

def addRandomAsteroid(xrel, yrel, zrel ):

    xran = (xrel + 40, xrel + 100)
    yran = (yrel - 50, yrel + 50)
    zran = (zrel - 50, zrel + 50)

    x = random.randint(xran[0], xran[1])
    y = random.randint(yran[0], yran[1])
    z = random.randint(zran[0], zran[1])
    return asteroid.Asteroid((x, y, z),(1.6,1.6))

def drawEdge(edge, verticies, rotation, color):
    points = []
    for x, y, z in (ship.verts[edge[0]], ship.verts[edge[1]]):
        x -= cam.x
        y -= cam.y
        z -= cam.z

        y, z = rotate2d(y, z, ship.rotation[1])
        x, z = rotate2d(x, z, ship.rotation[0])

        f = 200.0 / z

        x, y = x * f, y * f
        points += [(cx + int(x), cy + int(y))]
    if (points[0][0] > 0 and points[0][0] < w and points[0][1] > 0 and points[0][1] < h):
        pygame.draw.line(screen, (102, 255, 102), points[0], points[1], 1)
        return True
    else:
        return False

pygame.init()
w,h = 400, 400
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
cam = camera.Camera((0,0,0))
pygame.event.get()

ship = spaceShip.Ship((0, 0, -8), (1.6, 1.6))

asteroids = createRandomAsteroids(100, 0, -8)

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

    addAstCount = 0;

    for ast in asteroids:
        face_list = []
        face_color = []
        depth = []
        vert_list = []
        screen_coords = []

        for x, y, z in ast.verticies:
            x -= cam.x
            y -= cam.y
            z -= cam.z

            y, z = rotate2d(y, z, ast.rotation[1])
            x, z = rotate2d(x, z, ast.rotation[0])
            vert_list += [(x, y, z)]

            f = 200 / z
            x, y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]
            ast.update(dt, cam)

        for f in range(len(ast.faces)):
            face = ast.faces[f]

            on_screen = False
            for i in face:
                x, y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    on_screen = True
                    break

            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [ast.colorsApparent[f]]

                depth += [sum(sum(vert_list[j][i] for j in face) ** 2 for i in range(3))]

            order = sorted(range(len(face_list)), key=lambda i: depth[i], reverse=1)
            for i in order:
                try:
                    pygame.draw.polygon(screen, face_color[i], face_list[i])
                except:
                    pass

        if(ast.x  > (cam.x + 2 )):

            if(getDistance(ast.x, ast.y, ast.z, ship.x , ship.y, ship.z ) < (ast.size) ):
                running = False
                print (str(ast.x) + " " + str(ast.y) + " " + str(ast.z) + " ")
                print(str(ship.x) + " " + str(ship.y) + " " + str(ship.z) + " ")
                print(str(ship.rotation[0]) + " " + str(ship.rotation[1]))
                ast.color = (255, 0 ,0)
                print(ast.size)

        else:
            asteroids.remove(ast)
            addAstCount +=1

    asteroids.reverse()
    for i in range(addAstCount):
        asteroids.append(addRandomAsteroid(int(ship.x), int(ship.y), int(ship.z)))

    key = pygame.key.get_pressed()

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

                y, z = rotate2d(y, z, bullet.rotation[1])
                x, z = rotate2d(x, z, bullet .rotation[0])
                if(z != 0):
                    f = 200 / z
                    x, y = x * f, y * f
                points += [(cx + int(x), cy + int(y))]

            pygame.draw.line(screen, (255, 255, 153), points[0], points[1], 1)

            bullet.update(dt)
        if(bullet.x > bullet.destruct):
            bulletExists = False

    for edge in ship.edges:
        drawEdge(edge, ship.verts, ship.rotation, (102,255,102))

    ship.update(dt, key)
    cam.update1(ship)



input("complete")
pygame.display.quit()
sys.exit()
