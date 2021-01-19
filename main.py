import pygame
from enitities import Player, Enemy

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPACE_BG = (40, 36, 53)

player_img = 'player_ship.png'
enemy_img = 'Alien.png'

player_sprite = pygame.image.load(player_img)
player_x = 370
player_y = 480

player = Player(player_x, player_y, player_sprite)

enemy_sprite = pygame.image.load(enemy_img)
enemy = Enemy(SCREEN_WIDTH/2 - 32, 32, enemy_sprite)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load('alien_sml.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Invaders')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left = 1
            elif event.key == pygame.K_d:
                player.right = 1
            elif event.key == pygame.K_SPACE:
                player.fire()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left = 0
            elif event.key == pygame.K_d:
                player.right = 0
    
    screen.fill(SPACE_BG)
    player.entity_state(screen, SCREEN_WIDTH)
    enemy.entity_state(screen, SCREEN_WIDTH)


    
    pygame.display.update()
