import pygame
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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000
        screen.fill(color = (0, 0, 0), rect=None, special_flags=0)
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()
    return dt

if __name__ == "__main__":
    main()
