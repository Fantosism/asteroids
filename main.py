import os

from shot import Shot

os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
  pygame.init()

  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  Shot.containers = (shots, updatable, drawable)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2

  Player(x, y)
  AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")

    for updatable_sprite in updatable:
      updatable_sprite.update(dt)

      if isinstance(updatable_sprite, Player):
        for asteroid in asteroids:
          if updatable_sprite.check_collision(asteroid):
            print("Game over!")
            sys.exit()

    for asteroid in asteroids:
      for shot in shots:
        if asteroid.check_collision(shot):
          asteroid.split()
          shot.kill()

    for drawable_sprite in drawable:
      drawable_sprite.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
  main()
