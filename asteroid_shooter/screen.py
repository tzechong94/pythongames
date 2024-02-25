import pygame, sys
from random import randint, uniform

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

def meteor_update(meteor_list, speed = 200):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        # rect.y += round(speed * dt)
        # print(rect.y)
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)

# def random_x():
#     return random.randint(0, WINDOW_WIDTH)

def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text,True,'white')
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(background_surf, 'white', text_rect.inflate(30,30), width=8, border_radius=5)

def laser_timer(can_shoot, duration = 1000):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

#game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter w/o classes")
clock = pygame.time.Clock()

# ship import
ship_surf = pygame.image.load('graphics/ship.png').convert_alpha() # png doesnt run very fast
# ship_reversed_surf = pygame.transform.flip(ship_surf, False, True)
# ship_surf_scaled = pygame.transform.scale(ship_surf, (600,50))
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

# background import
background_surf = pygame.image.load('graphics/background.png').convert() # png doesnt run very fast

# laser import
laser_surf = pygame.image.load('graphics/laser.png').convert()
# laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
laser_list = []

# laser timer
can_shoot = True
shoot_time = None

# import text
font = pygame.font.Font('graphics/subatomic.ttf',50)

# import_sound
laser_sound = pygame.mixer.Sound('sounds/laser.ogg')
explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
background_music = pygame.mixer.Sound('sounds/music.wav')
background_music.play(loops=-1)
# meteor
# exercise:
# import the meteor surface
meteor_surf = pygame.image.load('graphics/meteor.png').convert_alpha()
meteor_list = []
# create a meteor using the repeated timer
# update all of the meteor rects inside of the meteor list
# draw all of the meteors
# copy the lasre logic except the meteors should move down

# meteor time
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# drawing
# test_rect = pygame.Rect(100,200,400,500) # can create rect with surface (l,t,w,h)


while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x in the window
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot: # 0.5 seconds of delay before we can shoot again
            # laser
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)

            # time logic
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

            # play laser sound
            laser_sound.play()


        if event.type == meteor_timer:
            # random position
            x_pos = randint(-100, WINDOW_WIDTH+100)
            y_pos = randint(-100, -50)
            meteor_rect = meteor_surf.get_rect(center = (x_pos,y_pos))

            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rect, direction))
            print('meteor')


    # framerate limit before the updates
    dt = clock.tick(120) / 1000 # never faster than 60 (returns the delta time) use seconds
    # clock.get_fps()


    # # MOUSE INPUT
    # print(pygame.mouse.get_pos())
    # print(pygame.mouse.get_pressed())
    ship_rect.center = pygame.mouse.get_pos()
   
    # 2. updates

    # move laser update
    laser_update(laser_list)
    # move meteor
    meteor_update(meteor_list)
    can_shoot = laser_timer(can_shoot,400)

    # meteor ship collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()

    # laser meteor collisions
    # we need two for loops -> one for the meteor and one for the laser
    # exercise: loop over both lists and get any kind of collision
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                laser_list.remove(laser_rect)
                meteor_list.remove(meteor_tuple)
                explosion_sound.play()

    # laser_rect.y += round(200 * dt)


    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(background_surf, (0,0)) # 
    # display_surface.blit(laser_surf, laser_rect)
    # for loop that draws the laser surface where the rects are
    display_score()
    #rect drawing
    # pygame.draw.rect(display_surface, 'purple', test_rect, width=10, border_radius=15)
    # pygame.draw.lines(display_surface, 'red', False, [(0,0), (200,50), (300,100)], width=1)
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)
    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])
    display_surface.blit(ship_surf, ship_rect)

    # 3. update the display surface
    pygame.display.update()
