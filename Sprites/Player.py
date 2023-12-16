import pygame
import json


with open('config.json', 'r') as cfg:
    config = json.load(cfg)
class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("./assets/PacMan.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 1
        self.points = 0
        self.rect.center = (
            75, 75
        )

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def update(self):
        self.x = 0
        self.y = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y = -5
        if key[pygame.K_s]:
            self.y = 5
        if key[pygame.K_a]:
            self.x = -5
        if key[pygame.K_d]:
            self.x = 5