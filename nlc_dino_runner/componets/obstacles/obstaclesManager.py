import random

import pygame

from nlc_dino_runner.componets.obstacles.bird import Bird
from nlc_dino_runner.componets.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        num_aux = random.randint(0, 2)
        if len(self.obstacles_list) == 0:
            if num_aux == 0:
                self.obstacles_list.append(Cactus(SMALL_CACTUS))
            elif num_aux == 1:
                self.obstacles_list.append(Cactus(LARGE_CACTUS))
            elif num_aux == 2:
                self.obstacles_list.append(Bird(BIRD))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)

            pygame.time.delay(2500)
            game.playing = False
            game.death_counts += 1
            break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []

