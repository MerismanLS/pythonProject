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
            300, 300
        )

    def update(self, *args, **kwargs):
        key = pygame.key.get_pressed()

        # управление по Y
        if key[pygame.K_w]:
            self.y = self.y + self.speed
        if key[pygame.K_s]:
            self.y = self.y - self.speed
        # управление по X
        if key[pygame.K_a]:
            self.x = self.x + self.speed
        if key[pygame.K_d]:
            self.x = self.x - self.speed