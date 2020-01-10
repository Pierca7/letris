from collections import namedtuple
import pygame
from pygame.locals import *
pygame.init()

TAMANO_LETRA = 20
TAMANO_LETRA_GRANDE = 30
FPS_INICIAL = 3
TIEMPO_MAX = 600
VELOCIDAD = 20
MENU_FONT_GRANDE = pygame.font.Font("SpaceMono-Regular.ttf", 60)
MENU_FONT_MEDIO = pygame.font.Font("SpaceMono-Regular.ttf", 45)
MENU_FONT = pygame.font.Font("SpaceMono-Regular.ttf", 30)

ANCHO = 400
ALTO = 600
COLOR_LETRA = (0, 0, 0)
COLOR_LETRAS = (255, 100, 100)
COLOR_FONDO = (200, 200, 200)
COLOR_TEXTO = (255, 70, 70)
COLOR_TIEMPO_FINAL = (200, 20, 10)
