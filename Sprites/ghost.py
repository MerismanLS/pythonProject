import copy
import pygame
import json
import utils

with open('config.json', 'r') as cfg:
    config = json.load(cfg)
display_mask = pygame.mask.from_surface(pygame.Surface((config["width"], config["height"])))


class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/ghost.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed_x = 4
        self.speed_y = 4
        self.rect.center = (
            925, 925
        )

    def update(self, player, *args):

        __map: list[list[int]] = args[0]
        virtual_rect = copy.deepcopy(self.rect)

        points = [
            virtual_rect.topleft, virtual_rect.topright, virtual_rect.bottomleft, virtual_rect.bottomright
        ]

        x_player, y_player = player.rect.center  # (10, 20)
        x_mob, y_mob = self.rect.center

        move_right = utils.lenght(x_player, y_player, x_mob + self.speed_x, y_mob)
        move_left = utils.lenght(x_player, y_player, x_mob - self.speed_x, y_mob)
        move_up = utils.lenght(x_player, y_player, x_mob, y_mob - self.speed_y)
        move_down = utils.lenght(x_player, y_player, x_mob, y_mob + self.speed_y)
        stay_here = utils.lenght(x_player, y_player, x_mob, y_mob)

        min_len = min(move_left, move_right, stay_here, move_down, move_up)
        if min_len == move_left:
            virtual_rect.x -= self.speed_x
        if min_len == move_right:
            virtual_rect.x += self.speed_x
        if min_len == move_up:
            virtual_rect.y -= self.speed_y
        if min_len == move_down:
            virtual_rect.y += self.speed_y

        # for point in points:
        #     x, y = point[0] // 50, point[1] // 50
        #     if __map[y][x] == 1:
        #         break
        # else:
        self.rect.center = virtual_rect.center






    # def compute_move(self, player, *args):
    #     __map: list[list[int]] = args[0]
    #     virtual_rect = copy.deepcopy(self.rect)
    #
    #     points = [
    #         virtual_rect.topleft, virtual_rect.topright, virtual_rect.bottomleft, virtual_rect.bottomright
    #     ]
    #
    #     x_player, y_player = player.rect.center  # (10, 20)
    #     x_mob, y_mob = self.rect.center
    #
    #     move_right = utils.lenght(x_player, y_player, x_mob + self.speed_x, y_mob)
    #     move_left = utils.lenght(x_player, y_player, x_mob - self.speed_x, y_mob)
    #     move_up = utils.lenght(x_player, y_player, x_mob, y_mob - self.speed_y)
    #     move_down = utils.lenght(x_player, y_player, x_mob, y_mob + self.speed_y)
    #     stay_here = utils.lenght(x_player, y_player, x_mob, y_mob)
    #
    #     min_len = min(move_left, move_right, stay_here, move_down, move_up)
    #     if min_len == move_left:
    #         self.rect.x -= self.speed_x
    #     if min_len == move_right:
    #         self.rect.x += self.speed_x
    #     if min_len == move_up:
    #         self.rect.y -= self.speed_y
    #     if min_len == move_down:
    #         self.rect.y += self.speed_y
    #
    #
    #
    #     for point in points:
    #         x, y = point[0] // 50, point[1] // 50
    #         if __map[y][x] == 1:
    #             break
    #     else:
    #         self.rect.center = virtual_rect.center
