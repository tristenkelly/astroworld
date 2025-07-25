from circleshape import *
import random
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        old_radius = self.radius
        random_angle = random.uniform(20, 50)
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid1 = Asteroid(self.position.x, self.position.y, old_radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, old_radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2

        
            

