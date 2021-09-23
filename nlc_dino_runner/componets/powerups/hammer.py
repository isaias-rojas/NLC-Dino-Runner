import random

from nlc_dino_runner.componets.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT


class Hammer(PowerUp):

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.hammer_counter = 0
        super().__init__(self.image, self.type)

    def set_pos_hammer(self, dino_rect):
        self.rect.x = dino_rect.x
        self.rect.y = dino_rect.y

    def draw_hammer(self, screen):
        screen.blit(self.image, self.rect)

    def update_hammer(self, game_speed, powerup):
        self.rect.x += game_speed
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -200
            powerup.throwing_hammer = False

    def reset(self):
        self.hammer_counter = 0
        self.rect.y = random.randint(100, 150)
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
