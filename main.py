from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player, Shot
import pygame
from constants import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots,updatable,drawable)


    clock = pygame.time.Clock()
    dt=0
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    field = AsteroidField()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over!")
                game_over=True
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()
