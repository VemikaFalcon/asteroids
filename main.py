import pygame
import sys
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, calculate_points
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particle import Particle


def main() -> None:
    pygame.init()
    pygame.font.init()
    score_font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particle = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    Particle.containers = (updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0.0
    current_score = 0
    lives = 3

    def create_explosion(position, groups):
        for _ in range(20): # Number of particles
            # Generate a random direction and speed
            random_velocity = pygame.Vector2(0, 1).rotate(random.uniform(0, 360))
            random_velocity *= random.uniform(50, 150)
        
            particle = Particle(position.x, position.y, random_velocity)
            # Add to your sprite groups so they update and draw
            for group in groups:
                group.add(particle)    

    while True:
        # log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        score_surface = score_font.render(f"Score: {current_score}", True, ("white"))
        screen.blit(score_surface, (10, 10))
        lives_surface = score_font.render(f"Lives: {lives}", True, ("white"))
        screen.blit(lives_surface, (SCREEN_WIDTH - 120, 10))
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    # log_event("asteroid_shot")
                    create_explosion(asteroid.position, [updatable, drawable])
                    shot.kill()
                    current_score += calculate_points(asteroid.radius)
                    asteroid.split()
        for asteroid in asteroids:
            if player.invulnerable_timer <= 0 and asteroid.collides_with(player):
                # log_event("player_hit")
                lives -= 1
                if lives > 0:
                    player.respawn()
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    player.velocity = pygame.Vector2(0, 0)
                else:
                    print("Game over!")
                    print(f"Final Score: {current_score}")
                    sys.exit()
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
