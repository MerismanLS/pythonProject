import pygame
import json

with open('config.json', 'r') as cfg:
    config = json.load(cfg)
class Cookies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(config["Yellow"])
        self.rect = self.image.get_rect()
        self.rect.center = (
            0, 0
        )

    def update(self):
        pass