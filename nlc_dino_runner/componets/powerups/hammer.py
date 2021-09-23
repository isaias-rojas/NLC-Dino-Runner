from nlc_dino_runner.componets.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH


class Hammer(PowerUp):

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

    def draw(self, screen):
        self.rect.y = 285
        screen.blit(self.image, self.rect)

    def update(self, player, game_speed=30):
        self.rect.x -= game_speed
        if self.rect.x > SCREEN_WIDTH:
            player.hammer = False
