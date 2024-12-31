import pygame
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_SPAWN_RATE, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  clock = pygame.time.Clock()
 
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updatable, drawable)

  newPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # Game Loop
  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return  
    screen.fill("black")
    for object in updatable: 
      object.update(dt)
    for object in drawable: 
      object.draw(screen)
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
  
  

if __name__ == "__main__":
  main()