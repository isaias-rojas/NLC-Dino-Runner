import random
import pygame

from nlc_dino_runner.componets.obstacles.text_utils import get_centered_message
from nlc_dino_runner.componets.powerups.hammer import Hammer
from nlc_dino_runner.componets.powerups.shield import Shield
from nlc_dino_runner.utils.constants import SHIELD_TYPE, DEFAULT_TYPE, HAMMER_TYPE


class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))
        self.throwing_hammer = False
        self.hammer = Hammer()

    def reset_power_ups(self, points, player):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points
        self.hammer.reset()
        player.hammer = False
        player.type = DEFAULT_TYPE

    def generate_power_ups(self, points, player):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating power")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                if player.type == DEFAULT_TYPE:
                    self.power_ups.append(random.choice([Shield(), Hammer()]))

    def update(self, points, game_speed, player):
        self.generate_power_ups(points, player)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                player.type = power_up.type
                if power_up.type == SHIELD_TYPE:
                    print("sss")
                    power_up.start_time = pygame.time.get_ticks()
                    player.hammer = False
                    player.shield = True
                    player.show_text = True
                    player.type = power_up.type
                    power_up.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                if power_up.type == HAMMER_TYPE:
                    self.power_ups.remove(power_up)
                    print("x")
                    player.shield = False
                    player.hammer = True
                    player.type = power_up.type
                    self.hammer.hammer_counter = 5

        user_input = pygame.key.get_pressed()

        if user_input[pygame.K_SPACE] and player.hammer and not self.throwing_hammer and self.hammer.hammer_counter > 0:
            self.throwing_hammer = True
            self.hammer.set_pos_hammer(player.dino_rect)
            self.hammer.hammer_counter -= 1

        if self.throwing_hammer:
            self.hammer.update_hammer(game_speed, self)

    def get_hammer(self):
        return self.hammer

    def check_hammer(self, screen, player):
        if self.hammer:
            print("x")
            if self.hammer.hammer_counter == 0:
                player.type = DEFAULT_TYPE
                self.hammer.reset()
                player.hammer = False
            else:
                if player.show_text:
                    text, text_rect = get_centered_message(
                        f'Hammers remain: {self.hammer.hammer_counter}',
                        width=500,
                        height=40,
                        size=20
                    )
                    screen.blit(text, text_rect)

    def draw(self, screen, player):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def draw_hammers_remains(self, screen, player):
        if self.throwing_hammer:
            self.hammer.draw_hammer(screen)
            self.check_hammer(screen, player)
