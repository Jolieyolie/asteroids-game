import pygame
import random
from circleshape import CircleShape
from player import Player
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, group=None):
        super().__init__((x, y), (0, 0), radius)
        self.radius = radius
        self.group = group
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position, new_radius, new_velocity1 * 1.2)
            new_asteroid2 = Asteroid(self.position, new_radius, new_velocity2 * 1.2)
            self.group.add(new_asteroid1)
            self.group.add(new_asteroid2)

    
