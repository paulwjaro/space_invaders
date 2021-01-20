import pygame
from pygame import mixer
import enitities
from enitities import Player, Enemy

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPACE_BG = (40, 36, 53)
FONT = pygame.font.Font('SourceCodePro-Regular.ttf', 24)
mixer.music.load('through space.ogg')
mixer.music.play(-1)

fire_fx = mixer.Sound('gun.wav')
explosion_fx = mixer.Sound('explode.wav')


def explosion():
    explosion_fx.play()


def show_score(x, y, _score):
    score_display = FONT.render(f"Score: {_score}", True, (255, 255, 255))
    screen.blit(score_display, (x, y))


level_started = False
enemies = []
enemy_queue = 3

player_img = 'player_ship.png'
enemy_img = 'Alien.png'

player_sprite = pygame.image.load(player_img)
player_x = 370
player_y = 480

player = Player(player_x, player_y, player_sprite)

enemy_sprite = pygame.image.load(enemy_img)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load('alien_sml.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Invaders')

running = True

while running:

    score = enitities.score
    if not level_started:
        for i in range(enemy_queue):
            enemies.append(Enemy(-96 * i, 32, enemy_sprite))
        level_started = True

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
                fire_fx.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left = 0
            elif event.key == pygame.K_d:
                player.right = 0
    
    screen.fill(SPACE_BG)
    show_score(600, 32, score)
    player.entity_state(screen, SCREEN_WIDTH, enemies, explosion)
    if len(enemies) != 0:
        for enemy in enemies:
            enemy.entity_state(screen, SCREEN_WIDTH)

    pygame.display.update()
