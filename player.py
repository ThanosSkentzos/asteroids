from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame

class Player(CircleShape):
    def __init__(self,x,y) -> None:
        super().__init__(x,y,PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(),2)
