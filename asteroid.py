import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector_one = self.velocity.rotate(angle)
            vector_two = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS


            spawn_1 = Asteroid(self.position.x, self.position.y, radius)
            spawn_1.velocity = vector_one * 1.2
            spawn_2 = Asteroid(self.position.x, self.position.y, radius)
            spawn_2.velocity = vector_two * 1.2