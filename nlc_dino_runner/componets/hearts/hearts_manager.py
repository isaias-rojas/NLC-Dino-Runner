from componets.hearts.heart import Hearts
from utils.constants import HEARTS_COUNTER


class HeartsManager:

    def __int__(self):
        self.hearts_counter = HEARTS_COUNTER

    def draw(self, screen):
        x_position: int = 60
        for counter in range(0, self.hearts_counter):
            heart = Hearts(x_position)
            x_position += 30
            heart.draw(screen)

    def reset_counter_hearts(self):
        self.hearts_counter = HEARTS_COUNTER


