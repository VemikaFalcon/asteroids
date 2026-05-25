import pygame

pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
LINE_WIDTH = 2

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_ACCELERATION = 200

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

SHOT_RADIUS = 5
SHOT_LIFETIME = 2.0
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3

SCORING_TABLE = [
    (ASTEROID_MIN_RADIUS, 100),
    (ASTEROID_MIN_RADIUS * 2, 70),
    (float('inf'), 50)
]

def calculate_points(radius):
    for max_radius, score in SCORING_TABLE:
        if radius <= max_radius:
            return score
    return 0