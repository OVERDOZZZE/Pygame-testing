import random
import pygame

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption('Nurdan')
pygame.display.set_icon(pygame.image.load('images/icon.png').convert_alpha())


background = pygame.image.load('images/background.png').convert_alpha()
player = pygame.image.load('images/player_right/right_0.png').convert_alpha()
walk_right = [
    pygame.image.load('images/player_right/right_0.png').convert_alpha(),
    pygame.image.load('images/player_right/right_1.png').convert_alpha(),
    pygame.image.load('images/player_right/right_2.png').convert_alpha(),
    pygame.image.load('images/player_right/right_3.png').convert_alpha()
]

walk_left = [
    pygame.image.load('images/player_left/left_0.png').convert_alpha(),
    pygame.image.load('images/player_left/left_1.png').convert_alpha(),
    pygame.image.load('images/player_left/left_2.png').convert_alpha(),
    pygame.image.load('images/player_left/left_3.png').convert_alpha(),
]


player_animation_count = 0
background_x = 0
ghost_list = []

ghost = pygame.image.load('images/ghost2.png').convert_alpha()
suriken = pygame.image.load('images/suriken.png').convert_alpha()

background_sound = pygame.mixer.Sound('sounds/background_sound.mp3')
background_sound.play()

#animation player

player_speed = 5
player_x = 50
player_y = 250

suriken_x = player_x

is_jump = False
jump_count = 7

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)

running = True  
while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 618, 0))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    if ghost_list:
        for i in ghost_list:
            screen.blit(ghost, i)
            i.x -= 4
            if player_rect.colliderect(i):
                # print('Game over')
                pass

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        screen.blit(walk_left[player_animation_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_animation_count], (player_x, player_y))

    if keys[pygame.K_d] and player_x < 400:
        player_x += player_speed
    elif keys[pygame.K_a] and player_x > 20:
        player_x -= player_speed

    if not is_jump:
        if keys[pygame.K_w]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    if player_animation_count == 3:
        player_animation_count = 0
    else:
        player_animation_count += 1

    background_x -= 2
    if background_x == -618:
        background_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list.append(ghost.get_rect(topleft=(620, 250)))

    clock.tick(30)








