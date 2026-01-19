import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position = self.position + self.velocity * dt
    def split(self,):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(split_angle)
            velocity2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_part= Asteroid(self.position.x,self.position.y,new_radius)
            second_part= Asteroid(self.position.x,self.position.y,new_radius)
            first_part.velocity = velocity1*1.2
            second_part.velocity = velocity2*1.2
