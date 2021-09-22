import pygame

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

BLACK_COLOR = (0, 0, 0)
FONT_STYLE = 'freesansbold.ttf'


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render("Score: " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (100, 50)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2, size=30):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect


def get_centered_score(points, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    score = font.render("Your score is " + str(points), True, BLACK_COLOR)
    score_rect = score.get_rect()
    score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    return score, score_rect
