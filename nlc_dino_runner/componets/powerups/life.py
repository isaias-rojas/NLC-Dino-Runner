from nlc_dino_runner.componets.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import LIFE, DEFAULT_TYPE


class Life(PowerUp):
    def __init__(self):
        self.image = LIFE
        self.type = DEFAULT_TYPE  # manera de usar
        super().__init__(self.image, self.type)
