import pygame

from nlc_dino_runner.componets.dino import Dino
from nlc_dino_runner.componets.hearts.hearts_manager import HeartsManager
from nlc_dino_runner.componets.obstacles import text_utils
from nlc_dino_runner.componets.obstacles.cactus import Cactus
from nlc_dino_runner.componets.obstacles.obstacles import Obstacles
from nlc_dino_runner.componets.obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.componets.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, \
    LARGE_CACTUS, RUNNING, FINAL_SCREEN

WHITE_COLOR = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False  # no estamos jugando aun cuando se inicializa el juego
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.game_speed = 20
        self.player = Dino()
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.hearts_manager = HeartsManager()
        self.points = 0
        self.running = True
        self.death_counts = 0

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        self.screen.fill(WHITE_COLOR)
        if self.death_counts == 0:
            self.print_menu_elements(True)
        elif self.death_counts > 0:
            self.print_menu_elements(False)

        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.hearts_manager.reset_counter_hearts()
        self.points = 0
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(WHITE_COLOR)

        self.draw_background()
        self.hearts_manager.draw(self.screen)
        self.score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invisibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        # la imagen se mueve
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

    def print_menu_elements(self, start=False):
        half_screen_height = SCREEN_HEIGHT // 2
        if start:
            messages = "Press any Key to Start"
        else:
            messages = "Press any Key to ReStart"
            death_score, death_score_rect = text_utils.get_centered_message("Death Count: " + str(self.death_counts),
                                                                            height=half_screen_height + 50)
            score, score_rect = text_utils.get_score_element(self.points)
            score_rect.center = (SCREEN_WIDTH // 2, half_screen_height + 100)
            self.screen.blit(death_score, death_score_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(FINAL_SCREEN, ((SCREEN_WIDTH // 2) - 190, half_screen_height - 200))

        text, text_rect = text_utils.get_centered_message(messages)
        self.screen.blit(text, text_rect)
        self.screen.blit(ICON, (SCREEN_WIDTH // 2 - 40, half_screen_height - 150))
