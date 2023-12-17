import json
import pygame
from Sprites.Player import Player
from Sprites.Cookies import Cookies
from Sprites.Ghost import Ghost
from Sprites.Wall import Wall
from Sprites.Lava import Lava
from maze import maze


with open('config.json', 'r') as cfg:
    config = json.load(cfg)

pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode((config['width'], config['height']))

player = Player()
player_sprite_group = pygame.sprite.Group()
player_sprite_group.add(player)

ghost = Ghost()
ghost_sprite_group = pygame.sprite.Group()
ghost_sprite_group.add(ghost)

lava_sprite_group = pygame.sprite.Group()
cookies_sprite_group = pygame.sprite.Group()
wall_sprite_group = pygame.sprite.Group()


running = True


def rendermaze(maze):
    x = 0
    y = 0
    for row in maze:
        for block in row:
            if block == 0:
                cookies = Cookies()
                cookies_sprite_group.add(cookies)
                cookies.rect.center = (
                    x + 25, y + 25
                )
                pygame.draw.rect(screen, config["Black"], (x, y, 50, 50))
            elif block == 1:
                # 1 = wall
                wall = Wall()
                wall_sprite_group.add(wall)
                wall.rect.center = (
                    x + 25, y + 25
                )
            x = x + 50
        y = y + 50
        x = 0


def lavaappear(maze):
        x = 0
        y = 0
        for row in maze:
            for block in row:
                if block == 0:
                    lava = Lava()
                    lava_sprite_group.add(lava)
                    lava.rect.center = (
                        x + 25, y + 25
                    )
                x = x + 50
            y = y + 50
            x = 0


clock = pygame.time.Clock()

time = 8 * config['framerate']
score = 0
rendermaze(maze)

while running:
    clock.tick(config['framerate'])
    if time == 0:
        running = False
    if player.points == 200:
        running = False
    if player.health == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.event = lavaappear(maze)
    pygame.time.set_timer(lavaappear(maze), 1000)

    eats = pygame.sprite.groupcollide(player_sprite_group, cookies_sprite_group, False, True)
    if eats:
        player.points += 1

    hits = pygame.sprite.groupcollide(player_sprite_group, ghost_sprite_group, False, False)
    if hits:
        player.health -= 1

    player_sprite_group.update(maze)
    cookies_sprite_group.update()
    wall_sprite_group.update()

    ghost_sprite_group.update(player, maze)
    screen.fill(config['Black'])

    points = font.render(f"Points: {player.points}", True, (255, 255, 255))
    screen.blit(points, (1100, 75))

    clock = pygame.time.Clock()
    counter = 10
    while counter > 0:
         counter -= 1
    time = font.render(f"Time left: {counter}", True, (255, 255, 255))
    screen.blit(time, (1100, 150))

    player_sprite_group.draw(screen)
    cookies_sprite_group.draw(screen)
    wall_sprite_group.draw(screen)
    ghost_sprite_group.draw(screen)

    pygame.display.flip()

pygame.quit()
