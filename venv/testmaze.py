import json
from maze import maze
import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

with open("config.json") as cfg:
    config = json.load(cfg)

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)

maze=[[1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,1,0,1,1,0,1,0,1],
      [1,0,1,0,1,1,0,1,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,1,0,1,1,0,1,0,1],
      [1,0,1,0,1,1,0,1,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1],]

def renderMaze(maze):
    x = 0
    y = 0
    for row in maze:
        for block in row:
            # block dimension 60*60
            # 0 represents movable cell
            if block == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 100, 100))
            # 1 represents wall
            elif block == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
            # 2 represents destination
            elif block == 2:
                pygame.draw.rect(screen, (255, 255, 0), (x, y, 100, 100))

            # to display the starting cell
            elif block == 3:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, 100, 100))

            x = x + 100
        y = y + 100
        x = 0

pygame.display.update()

clock = pygame.time.Clock()
running = True

time = 8 * config['framerate']
score = 0



while running:
    clock.tick(config['framerate'])
    if time == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
