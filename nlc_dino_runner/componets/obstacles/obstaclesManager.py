import random

import pygame

from componets.obstacles.bird import Bird
from componets.obstacles.cactus import Cactus
from utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, GAME_OVER_SOUND, COLLIDE_SOUND, LOST_LIFE


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game, joystick=None):
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

            offset = (obstacle.rect.x - game.player.dino_rect.x, obstacle.rect.y - game.player.dino_rect.y)
            if game.player.mask.overlap(obstacle.mask, offset):
                if game.player.shield:
                    pygame.mixer.Sound.play(COLLIDE_SOUND)
                    self.obstacles_list.remove(obstacle)
                else:
                    pygame.mixer.Sound.play(LOST_LIFE)
                    game.hearts_manager.hearts_counter -= 1

                    if joystick:
                        joystick.rumble(1.0, 1.0, 500)

                    if game.hearts_manager.hearts_counter > 0:
                        self.obstacles_list.remove(obstacle)
                    else:
                        pygame.time.delay(1000)
                        pygame.mixer.Sound.play(GAME_OVER_SOUND)
                        game.playing = False
                        game.death_counts += 1
                        break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
