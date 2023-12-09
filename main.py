import random
import json
import pygame
from Sprites.Player import Player
from maze import maze

f = open('config.json')
config = json.load(f)

pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)


player = pygame.sprite.Group()
player.add(Player())

running = True

def renderMaze(maze):
    x = 0
    y = 0
    for row in maze:
        for block in row:
            if block == 0:
            # 0 = wall
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))
            elif block == 1:
            # 1 = path
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))

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

    screen.fill(config['Black'])
    renderMaze(maze)
    time_rendered = font.render(f"Time: {time / config['framerate']}", True, (255, 255, 255))
    screen.blit(time_rendered, (10, 10))
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
