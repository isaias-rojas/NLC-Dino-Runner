from componets.powerups.powerup import PowerUp
from utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp):

    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE # manera de usar
        super().__init__(self.image, self.type)

