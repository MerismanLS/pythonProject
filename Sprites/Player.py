import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((90, 90, 90))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 1

        self.rect.center = (
            75, 75
        )

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