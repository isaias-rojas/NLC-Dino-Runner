from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class Obstacles(Sprite):

    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.type].get_rect()  # especifica que el self type defina que imagen
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles_list):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles_list.pop()

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], self.rect)
