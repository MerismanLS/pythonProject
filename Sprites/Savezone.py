import pygame
import json


with open('config.json', 'r') as cfg:
    config = json.load(cfg)
class Savezone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/savezone.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (
            0, 0
        )