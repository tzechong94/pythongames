import pygame, sys
from settings import WINDOW_WIDTH, WINDOW_HEIGHT 

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    dt = clock.tick() / 1000

    pygame.display.update()