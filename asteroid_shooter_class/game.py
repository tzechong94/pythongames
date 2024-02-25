import pygame, sys
from random import randint, uniform


#game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter w classes")
clock = pygame.time.Clock()



while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x in the window
            pygame.quit()
            sys.exit()

       
    # framerate limit before the updates
    dt = clock.tick() / 1000 
    # clock.get_fps()


    # drawing

    # 3. update the display surface
    pygame.display.update()
