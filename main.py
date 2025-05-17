import pygame
import random
from asteroid import Asteroid
from asteroidfield import *
from player import Player
from shot import *
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
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Assign containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # Create player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000  
        #Update all game objects     
        updatable.update(dt)
        # Collision detection
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return
        # Draw everything    
        screen.fill(color = (0, 0, 0), rect=None, special_flags=0)
        for obj in drawable:
            obj.draw(screen)

       
        pygame.display.flip()
    
    return dt


if __name__ == "__main__":
    main()
