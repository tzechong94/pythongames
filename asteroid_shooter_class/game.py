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

        # 4. Add a mask
        self.mask = pygame.mask.from_surface(self.image)

        #timer
        self.can_shoot = True
        self.shoot_time = None

        # sound
        self.laser_sound = pygame.mixer.Sound('sounds/laser.ogg')
    # create lots of other methods
    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
    
    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print('shoot laser')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            Laser(laser_group, self.rect.midtop)
            self.laser_sound.play()

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True
    
    def meteor_collision(self):
        if pygame.sprite.spritecollide(self,meteor_group,False, pygame.sprite.collide_mask):
            pygame.quit()
            sys.exit()

    def update(self):
        self.laser_timer()
        self.input_position()
        self.laser_shoot()
        self.meteor_collision()

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/laser.png').convert()
        self.rect = self.image.get_rect(midbottom = position)
        self.mask = pygame.mask.from_surface(self.image)
        # float based position
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 600

        #sound
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')


    def meteor_collision(self):
        if pygame.sprite.spritecollide(self,meteor_group,True,pygame.sprite.collide_mask):
            self.explosion_sound.play()
            self.kill()

    def update(self):
        self.position += (self.speed * self.direction * dt)
        self.rect.topleft = (round(self.position.x),round(self.position.y))

        if self.rect.bottom < 0:
            self.kill()

        self.meteor_collision()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)

        # randomize meteor size

        meteor_surf = pygame.image.load('graphics/meteor.png').convert_alpha()
        meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * uniform(0.5,1.5)
        self.scaled_surf = pygame.transform.scale(meteor_surf, meteor_size)
        self.image = self.scaled_surf
        self.rect = self.image.get_rect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(400,600)

        # rotation logic
        self.rotation = 0 
        self.rotation_speed = randint(20,50)
    
    def rotate(self):
        self.rotation += self.rotation_speed * dt
        rotated_surf = pygame.transform.rotate(self.scaled_surf, self.rotation)# can use rotozoom too
        # as compared to self.image 
        self.image = rotated_surf
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        # update mask when rect is updated

    def update(self):
        self.position += (self.speed * self.direction * dt)
        self.rect.topleft = (round(self.position.x),round(self.position.y))
        self.rotate()
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Score:
    def __init__(self):
        self.font = pygame.font.Font('graphics/subatomic.ttf', 50)

    def display(self):
        score_text = f'Score: {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(score_text, True, 'white')
        text_rect = text_surf.get_rect(midbottom = ((WINDOW_WIDTH/2), WINDOW_HEIGHT-80))
        display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(display_surface, 'white', text_rect.inflate(30,30), width=8,border_radius=5 )

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
meteor_group = pygame.sprite.Group()
# sprite creation
ship = Ship(spaceship_group)

spaceship_group.add(ship)

# timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# score
score = Score()

# music 
bg_music = pygame.mixer.Sound('sounds/music.wav')
bg_music.play(loops=-1)
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x in the window
            pygame.quit()
            sys.exit()
        if event.type == meteor_timer:
            print('meteor')
            meteor_y_pos = randint(-150,-50)
            meteor_x_pos = randint(-100,WINDOW_WIDTH+100)
            Meteor(meteor_group, (meteor_x_pos,meteor_y_pos))

       
    # framerate limit before the updates
    dt = clock.tick() / 1000 
    # clock.get_fps()

    # background
    display_surface.blit(background_surface, (0,0))


    # update
    spaceship_group.update()
    laser_group.update()
    meteor_group.update()

    # score 
    score.display()

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)

    # drawing

    # 3. update the display surface
    pygame.display.update()
