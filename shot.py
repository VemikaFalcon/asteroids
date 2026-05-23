import pygame
from constants import LINE_WIDTH, SHOT_RADIUS, SHOT_LIFETIME
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.timer = SHOT_LIFETIME

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        self.wrap_position()
        self.timer -= dt
        if self.timer <= 0:
            self.kill()
