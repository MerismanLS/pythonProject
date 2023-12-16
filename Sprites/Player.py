import copy

import pygame
import json
import math

with open('config.json', 'r') as cfg:
    config = json.load(cfg)
display_mask = pygame.mask.from_surface(pygame.Surface((config["width"], config["height"])))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/PacMan.png")
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 5
        self.points = 0
        self.rect.center = (
            24, 24
        )

    def up(self, value):
        self.speed += value

    def down(self, value):
        self.speed -= value

    def update(self, *args):
        __map: list[list[int]] = args[0]
        virual_rect = copy.deepcopy(self.rect)
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            virual_rect.y += -5
        if key[pygame.K_s]:
            virual_rect.y += 5
        if key[pygame.K_a]:
            virual_rect.x += -5
        if key[pygame.K_d]:
            virual_rect.x += 5

        in_bounce = True
        points = [
            virual_rect.topleft, virual_rect.topright, virual_rect.bottomleft, virual_rect.bottomright
        ]
        for point in points:
            x, y = point[0] // 50, point[1] // 50
            if __map[y][x] == 1:
                break
        else:
            self.rect.center = virual_rect.center
