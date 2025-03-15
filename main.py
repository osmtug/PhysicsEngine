from circle import Circle
from grid import Grid
import numpy as np
import random
import pygame as pg

# ***** Press SPACE to generate red, green, and blue balls. Press ENTER to generate balls with a random color. ******

MAX_CIRCLE = 1500 # max number of circle
SPAWN_TIME = 0.05 # Ball spawn every SPAWN_TIME seconds

# pg setup
pg.init()
screen = pg.display.set_mode((1200, 500), pg.RESIZABLE)
clock = pg.time.Clock()
running = True
productCircle = True
dt = 0

l: list[Circle] = []

radius = 5
spawnTimer = 2000

nbCircle = 9

# l.append(Circle(x=100, y=260, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=110, y=200, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=110, y=300, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=65, y=200, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=50, y=200, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=50, y=300, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=134, y=300, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=154, y=250, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
# l.append(Circle(x=50, y=250, radius=10, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))

grid = Grid(10)

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE] and productCircle and nbCircle < MAX_CIRCLE and spawnTimer > SPAWN_TIME :
        l.append(Circle(x=100, y=350, radius=radius, color=(255, 0, 0), acceleration_x=2, acceleration_y=-1))
        l.append(Circle(x=110, y=250, radius=radius, color=(0, 255, 0), acceleration_x=2, acceleration_y=-1))
        l.append(Circle(x=120, y=300, radius=radius, color=(0, 0, 255), acceleration_x=2, acceleration_y=-1))
        nbCircle += 3
        spawnTimer = 0

    if keys[pg.K_RETURN]and productCircle and nbCircle < MAX_CIRCLE and spawnTimer > SPAWN_TIME: 
        l.append(Circle(x=100, y=350, radius=radius, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), acceleration_x=2, acceleration_y=-1))
        l.append(Circle(x=110, y=250, radius=radius, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), acceleration_x=2, acceleration_y=-1))
        l.append(Circle(x=120, y=300, radius=radius, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), acceleration_x=2, acceleration_y=-1))
        nbCircle += 3
        spawnTimer = 0


    spawnTimer += dt

    grid.build(l)

    # Vérification des collisions
    collisions = grid.check_collisions()

    for i in range(0, len(l), 1):
        
        l[i].update(dt)
        l[i].deplacer(screen.get_width(), screen.get_height(), dt)


        l[i].dessiner(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    if clock.get_fps() < 60:
        productCircle = False
    else :
        productCircle = True

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000


pg.quit()