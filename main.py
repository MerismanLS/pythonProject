import json
import random
import pygame
from utils import putinwin, fnafwin, fnafdeath, skaladeath, dsdeath, sigmawin, pobedawin
from Sprites.Player import Player
from Sprites.Cookies import Cookies
from Sprites.Wall import Wall
from Sprites.Lava import Lava
from Sprites.Savezone import Savezone
from Sprites.Meme import Meme
from maze import maze


with open('config.json', 'r') as cfg:
    config = json.load(cfg)

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
pygame.mixer.music.load("./assets/doom.mp3")
screen = pygame.display.set_mode((config['width'], config['height']))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

cookie_collect = pygame.mixer.Sound("./assets/сбор.ogg")
cookie_collect.set_volume(1.0)

player = Player()
player_sprite_group = pygame.sprite.Group()
player_sprite_group.add(player)

lava = Lava()
lava_sprite_group = pygame.sprite.Group()
lava_sprite_group.add(lava)

meme = Meme()
meme_sprite_group = pygame.sprite.Group()
meme_sprite_group.add(meme)

savezone_sprite_group = pygame.sprite.Group()
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
            elif block == 2:
                savezone = Savezone()
                savezone_sprite_group.add(savezone)
                savezone.rect.center = (
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
counter1 = random.randint(7, 15)
counter2 = random.randint(3, 7)

timing = 8 * config['framerate']
score = 0
rendermaze(maze)
runs = False
lavacoming = pygame.USEREVENT
pygame.time.set_timer(lavacoming, 1000)

while running:
    clock.tick(config['framerate'])
    if timing == 0:
        running = False
    if player.points == 200:
        num = random.randint(1, 4)
        if num == 1:
            putinwin()
            running = False
        elif num == 2:
            pobedawin()
            running = False
        elif num == 3:
            sigmawin()
            running = False
        else:
            fnafwin()
            running = False

    if player.health == 0:
        num = random.randint(1, 3)
        if num == 1:
            dsdeath()
            running = False
        elif num == 2:
            skaladeath()
            running = False
        else:
            fnafdeath()
            running = False

    for event in pygame.event.get():
        if event.type == lavacoming:
            if counter1 > 0:
                runs = False
                counter1 -= 1
            else:
                lavaappear(maze)
                if counter2 > 0:
                    runs = True
                    counter2 -= 1
                else:
                    lava_sprite_group.update(True)
                    if player.points <= 150:
                        if player.points <= 100:
                            counter1 = random.randint(7, 15)
                            counter2 = random.randint(3, 7)
                        else:
                            counter1 = random.randint(5, 10)
                            counter2 = random.randint(5, 7)
                    else:
                        counter1 = random.randint(3, 7)
                        counter2 = random.randint(5, 10)
        if event.type == pygame.QUIT:
            running = False

    eats = pygame.sprite.groupcollide(player_sprite_group, cookies_sprite_group, False, True)
    if eats:
        player.points += 1
        cookie_collect.play()


    hits = pygame.sprite.groupcollide(player_sprite_group, lava_sprite_group, False, False)
    if hits:
        player.health -= 1

    meme_sprite_group.update()
    player_sprite_group.update(maze)
    cookies_sprite_group.update()
    wall_sprite_group.update()
    savezone_sprite_group.update()
    lava_sprite_group.update(False)
    screen.fill(config['Black'])

    points = font.render(f"Points: {player.points}", True, (255, 255, 255))
    screen.blit(points, (1050, 75))
    motivation = font.render("JUST DO IT!!!", True, (255, 255, 255))
    screen.blit(motivation, (1050, 300))
    if runs == False:
        seconds = font.render(f"Lava is coming in {counter1}", True, (255, 255, 255))
        screen.blit(seconds, (1050, 150))
    else:
        seconds = font.render(f"Lava is here for {counter2}", True, (255, 255, 255))
        screen.blit(seconds, (1050, 150))

    meme_sprite_group.draw(screen)
    savezone_sprite_group.draw(screen)
    player_sprite_group.draw(screen)
    cookies_sprite_group.draw(screen)
    wall_sprite_group.draw(screen)
    lava_sprite_group.draw(screen)

    pygame.display.flip()

pygame.quit()
