import copy
import pygame
import json


with open('config.json', 'r') as cfg:
    config = json.load(cfg)
display_mask = pygame.mask.from_surface(pygame.Surface((config["width"], config["height"])))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/troll.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.health = 1
        self.points = 0
        self.rect.center = (
            75, 75
        )

    def update(self, *args):
        __map: list[list[int]] = args[0]
        virtual_rect = copy.deepcopy(self.rect)
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            virtual_rect.y += -5
        if key[pygame.K_s]:
            virtual_rect.y += 5
        if key[pygame.K_a]:
            virtual_rect.x += -5
        if key[pygame.K_d]:
            virtual_rect.x += 5

        points = [
            virtual_rect.topleft, virtual_rect.topright, virtual_rect.bottomleft, virtual_rect.bottomright
        ]

        for point in points:
            x, y = point[0] // 50, point[1] // 50
            if __map[y][x] == 1:
                break
        else:
            self.rect.center = virtual_rect.center
