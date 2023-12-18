import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/lava.jpg")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.rect.center = (
            -100, -100
        )

    def update(self, killing: bool):
        if killing == True:
            self.kill()
