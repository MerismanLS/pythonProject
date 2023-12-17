import pygame
import json
import random


with open('config.json', 'r') as cfg:
    config = json.load(cfg)
class Lava(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/lava.jpg")
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 1
        self.points = 0
        self.rect.center = (
            0, 0
        )

    def update(self, maze):
        pass
