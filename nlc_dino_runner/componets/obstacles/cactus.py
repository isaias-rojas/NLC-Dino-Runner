
#clase hija
import random

from nlc_dino_runner.componets.obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        #llamar al init de nuestro padre o metodos del padre
        super().__init__(image, self.type)
        self.rect.y = 315



