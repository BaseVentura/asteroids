import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_SPAWN_RATE, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  clock = pygame.time.Clock()
  dt = 0
  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return  
    pygame.Surface.fill(screen,(0,0,0 ))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()