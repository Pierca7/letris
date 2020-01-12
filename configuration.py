import pygame

from collections import namedtuple
from pygame.locals import *

pygame.init()

FONT_SIZE_SMALL = 20
FONT_SIZE_BIG = 30
FPS = 3
MAX_TIME = 600
SPEED = 20
MENU_FONT_SIZE_BIG = pygame.font.Font("SpaceMono-Regular.ttf", 60)
MENU_FONT_SIZE_REGULAR = pygame.font.Font("SpaceMono-Regular.ttf", 45)
MENU_FONT_SIZE_SMALL = pygame.font.Font("SpaceMono-Regular.ttf", 30)

HEIGHT = 400
WIDTH = 600
FONT_COLOR_WHITE = (0, 0, 0)
FONT_COLOR = (255, 100, 100)
BACKGROUND_COLOR = (200, 200, 200)
TEXT_COLOR = (255, 70, 70)
TIME_TEXT_COLOR = (200, 20, 10)
