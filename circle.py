import pygame as pg
import math

class Circle:
    def __init__(self, x, y, radius, color, acceleration_x=0, acceleration_y=0):
        self.x = x
        self.y = y
        self.x_old = x
        self.y_old = y
        self.radius = radius
        self.color = color
        self.acceleration_x = acceleration_x 
        self.acceleration_y = acceleration_y 

    def dessiner(self, fenetre):
        pg.draw.circle(fenetre, self.color, (self.x, self.y), self.radius)
    
    def update(self, dt):
        self.acceleration_y += 500

    def deplacer(self, largeur_fenetre, hauteur_fenetre, dt):

        

        if self.x + self.radius > largeur_fenetre:
            self.x = largeur_fenetre - self.radius
        elif self.x - self.radius < 0:
            self.x = self.radius

        if self.y + self.radius > hauteur_fenetre:
            self.y = hauteur_fenetre - self.radius
        velocity_x = self.x - self.x_old
        velocity_y = self.y - self.y_old

        self.x_old = self.x
        self.y_old = self.y

        self.x = self.x + velocity_x + self.acceleration_x * dt * dt
        self.y = self.y + velocity_y + self.acceleration_y * dt * dt
        
        

        self.acceleration_y = 0
        self.acceleration_x = 0
        
    def collision(self, otherCircle):
        distance = (self.x - otherCircle.x)**2 + (self.y - otherCircle.y)**2
        if distance < (self.radius + otherCircle.radius)**2:

            distance = math.sqrt(distance)

            axis_x = self.x - otherCircle.x
            axis_y = self.y - otherCircle.y

            if distance != 0:
                nx = axis_x / distance
                ny = axis_y / distance
            else:
                nx = 0
                ny = 0
            delta = self.radius + otherCircle.radius - distance

            self.x += 0.5 * delta * nx 
            self.y += 0.5 * delta * ny
            otherCircle.x -= 0.5 * delta * nx 
            otherCircle.y -= 0.5 * delta * ny


