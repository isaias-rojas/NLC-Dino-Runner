import random

import pygame

from nlc_dino_runner.componets.obstacles.bird import Bird
from nlc_dino_runner.componets.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, GAME_OVER_SOUND, COLLIDE_SOUND, LOST_LIFE


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        num_aux = random.randint(0, 2)
        if len(self.obstacles_list) == 0:
            if num_aux == 0:
                self.obstacles_list.append(Cactus(SMALL_CACTUS))
            elif num_aux == 1:
                cactus = Cactus(LARGE_CACTUS)
                cactus.rect.y = 290
                self.obstacles_list.append(cactus)
            elif num_aux == 2:
                self.obstacles_list.append(Bird(BIRD))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)

            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                self.obstacles_list.remove(obstacle)
                print("y")

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.dino_rect.colliderect(obstacle.rect):
                    if game.player.shield:
                        pygame.mixer.Sound.play(COLLIDE_SOUND)
                        self.obstacles_list.remove(obstacle)
                    else:
                        pygame.mixer.Sound.play(LOST_LIFE)
                        game.hearts_manager.hearts_counter -= 1
                        if game.hearts_manager.hearts_counter > 0:
                            self.obstacles_list.remove(obstacle)
                        else:
                            pygame.time.delay(2500)
                            pygame.mixer.Sound.play(GAME_OVER_SOUND)
                            game.playing = False
                            game.death_counts += 1
                            break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
