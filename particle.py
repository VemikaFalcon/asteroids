import pygame
import random
from constants import SHOT_LIFETIME

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.lifetime = random.uniform(0.1, 0.5) # They vanish quickly
        self.max_lifetime = SHOT_LIFETIME

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def draw(self, screen):
        ratio = self.lifetime / self.max_lifetime
        color_val = 100 + (155 * ratio)
        color = (color_val, color_val, color_val)

        # Draw a tiny dot or a small circle
        pygame.draw.circle(screen, color, self.position, 2)
