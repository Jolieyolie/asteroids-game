import pygame
import random
from asteroid import Asteroid
from asteroidfield import *
from player import Player
from constants import *

def main():
    # initialize the pygame module
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print(screen)
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000       
        updatable.update(dt)
        screen.fill(color = (0, 0, 0), rect=None, special_flags=0)
        for obj in drawable:
            obj.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        asteroid_field = AsteroidField()
        pygame.display.flip()
    pygame.quit()
    return dt


if __name__ == "__main__":
    main()
