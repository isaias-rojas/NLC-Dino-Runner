import pygame
import pygame.joystick

from pygame.sprite import Sprite
from componets.obstacles.text_utils import get_centered_message
from utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    RUNNING_HAMMER,
    DUCKING_HAMMER,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE, JUMPING_HAMMER, JUMP_SOUND, DUCK_SOUND)


class Dino(Sprite):
    X_POS = 80
    Y_POS = 285
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER
        }
        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER
        }
        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER
        }
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.mask = pygame.mask.from_surface(self.image)

        self.shield = False
        self.shield_time_up = 0
        self.show_text = False

        self.hammer = False
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

    def update(self, user_input, joystick=None):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        jump_button = joystick.get_button(0) if joystick else False  
        axis_y = joystick.get_axis(1) if joystick else 0  

        if user_input[pygame.K_DOWN] or axis_y > 0.5 and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
            pygame.mixer.Sound.play(DUCK_SOUND)
        elif user_input[pygame.K_UP] or jump_button or axis_y < -0.5 and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
            pygame.mixer.Sound.play(JUMP_SOUND)
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        
        self.image = self.run_img[self.type][self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image) 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        self.mask = pygame.mask.from_surface(self.image)  
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def check_invisibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show < 0:
                self.shield = False
                if self.type == SHIELD_TYPE:
                    self.type = DEFAULT_TYPE
            else:
                if self.show_text:
                    text, text_rect = get_centered_message(f'shield enabled for {time_to_show}', width=500, height=40,
                                                           size=20)
                    screen.blit(text, text_rect)

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
