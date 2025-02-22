from circle import Circle
import pygame as pg

# pg setup
pg.init()
screen = pg.display.set_mode((200, 500), pg.RESIZABLE)
clock = pg.time.Clock()
running = True
productCircle = True
dt = 0

l = []

radius = 5

l.append(Circle(x=100, y=260, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=110, y=200, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=110, y=300, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=200, y=200, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=50, y=200, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=50, y=300, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=200, y=300, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=200, y=250, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
l.append(Circle(x=50, y=250, radius=20, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))


player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    if productCircle :
        # l.append(ParticleOfWater(x=100, y=350, radius=radius, color=(255, 0, 0), acceleration_x=8, acceleration_y=-1))
        # l.append(ParticleOfWater(x=105, y=250, radius=radius, color=(0, 255, 0), acceleration_x=8, acceleration_y=-1))
        l.append(Circle(x=110, y=300, radius=radius, color=(0, 0, 255), acceleration_x=8, acceleration_y=-1))

    

    for i in range(0, len(l), 1):
        
        l[i].update(dt)
        l[i].deplacer(screen.get_width(), screen.get_height(), dt)

        for j in range(0, len(l), 1):
            if i != j:
                l[i].collision(l[j])

        l[i].dessiner(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    if clock.get_fps() < 80:
        productCircle = False
    else :
        productCircle = True

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000


pg.quit()