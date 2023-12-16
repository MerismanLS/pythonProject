import random
import json
import pygame
from Sprites.Player import Player
from Sprites.cookies import Cookies
from maze import maze2

with open('config.json', 'r') as cfg:
    config = json.load(cfg)

pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)

player = Player(screen)
player_sprite_group = pygame.sprite.Group()
player_sprite_group.add(player)

cookies = Cookies()
player_sprite_group.add(cookies)

running = True

def renderMaze(maze2):
    x = 0
    y = 0
    for row in maze2:
        for block in row:
            if block == 0:
            # 0 = path
                cookies = Cookies()
                player_sprite_group.add(cookies)
                cookies.rect.center = (
                    x + 25, y + 25
                )
                pygame.draw.rect(screen, config["Black"], (x, y, 50, 50))
            elif block == 1:
            # 1 = wall
                pygame.draw.rect(screen, config["Blue"], (x, y, 50, 50))
            else:
                player.rect.center = (x+25, y+25)

            x = x + 50
        y = y + 50
        x = 0

clock = pygame.time.Clock()

time = 8 * config['framerate']
score = 0

while running:
    player.update()
    clock.tick(config['framerate'])
    if time == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.is_collided_with(cookies):
        player.points += 1
        cookies.kill()


    player_sprite_group.update()
    screen.fill(config['Black'])
    renderMaze(maze2)
    points = font.render(f"Points: {player.points}", True, (255, 255, 255))
    screen.blit(points, (10, 30))
    time_rendered = font.render(f"Time: {time / config['framerate']}", True, (255, 255, 255))
    screen.blit(time_rendered, (10, 10))
    player_sprite_group.draw(screen)
    pygame.display.flip()

pygame.quit()
