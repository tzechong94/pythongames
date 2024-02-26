import pygame, sys
from random import randint, uniform

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        # 1. we have to init parent class
        super().__init__(groups) 

        # 2. need a surface -> image
        self.image = pygame.image.load('graphics/ship.png').convert_alpha()
        
        # 3. we need a rect
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        #timer
        self.can_shoot = True
        self.shoot_time = None
    # create lots of other methods
    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
    
    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print('shoot laser')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True
    
    def update(self):
        self.laser_timer()
        self.input_position()
        self.laser_shoot()

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/laser.png').convert()
        self.rect = self.image.get_rect(midbottom = position)
        self.position = position



#game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter w classes")
clock = pygame.time.Clock()

#background
background_surface = pygame.image.load("graphics/background.png").convert()

# sprite groups
spaceship_group = pygame.sprite.GroupSingle() # 1 sprite only
laser_group = pygame.sprite.Group()
# sprite creation
ship = Ship(spaceship_group)
laser = Laser(laser_group,(100,300))

laser_group.add(laser)
spaceship_group.add(ship)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x in the window
            pygame.quit()
            sys.exit()

       
    # framerate limit before the updates
    dt = clock.tick() / 1000 
    # clock.get_fps()

    # background
    display_surface.blit(background_surface, (0,0))

    # update
    spaceship_group.update()
    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    # drawing

    # 3. update the display surface
    pygame.display.update()
