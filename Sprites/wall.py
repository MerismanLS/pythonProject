import pygame
import json


with open('config.json', 'r') as cfg:
    config = json.load(cfg)
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/wall.png")
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 1
        self.points = 0
        self.rect.center = (
            0, 0
        )