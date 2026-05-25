import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.points = []
        num_points = 12
        for i in range(num_points):
            angle = (i / num_points) * 360
            distance = self.radius * random.uniform(0.7, 1.0)
            self.points.append((angle, distance))

    def draw(self, screen: pygame.Surface) -> None:
        draw_points = []
        for angle, distance in self.points:
            point_offset = pygame.Vector2(0, distance).rotate(angle)
            draw_points.append(self.position + point_offset)
        pygame.draw.polygon(screen, "white", draw_points, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        self.wrap_position()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_rotation1 = self.velocity.rotate(random_angle)
        new_rotation2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_rotation1 * 1.2
        new_asteroid2.velocity = new_rotation2 * 1.2

        
    