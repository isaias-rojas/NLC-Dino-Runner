from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART


class Hearts(Sprite):
    POS_Y = 15

    def __init__(self, pos_x):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.rect.x = self.pos_x
        self.rect.y = self.POS_Y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

