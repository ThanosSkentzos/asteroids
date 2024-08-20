from constants import ASTEROID_MIN_RADIUS
import pygame
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x,y)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity*dt
    def split(self):
        self.kill()

        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-1*angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x,self.position.y,new_radius)
        a2 = Asteroid(self.position.x,self.position.y,new_radius)
        a1.velocity = vel1*1.2
        a2.velocity = vel2*1.2
