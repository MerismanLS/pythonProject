import pygame

class Meme(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/meme.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (
            1318, 700
        )