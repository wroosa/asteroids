import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    dt = 0
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        # Update and draw sprites
        updatable.update(dt)

        # Check collisions
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()
            
            for bullet in bullets:
                if asteroid.collision_check(bullet):
                    asteroid.kill()
                    bullet.kill()

        # Draw sprites
        for sprite in drawable:
            sprite.draw(screen)
        
        
        # Logging
        Text = "Hellos"
        font = pygame.font.SysFont("arial", 36)
        text_surface = font.render(Text, True, (255, 255, 255))
        screen.blit(text_surface, (30, 30))

        # Render
        pygame.display.flip()
        dt = clock.tick()/1000

if __name__ == "__main__":
    main()
