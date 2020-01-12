import pygame

from pygame.locals import *
from configuration import *

def centerText(text, window):
    text_rec= text.get_rect()
    if window == "chica":
        posX= (HEIGHT-text_rec[2]) /2
        return posX
    if window == "grande":
        posX= (HEIGHT+400-text_rec[2]) /2
        return posX

def getPressedKey(key):
    if key == K_UP:
        return "up"
    elif key == K_DOWN:
        return "down"
    elif key == K_RIGHT:
        return "right"
    elif key == K_LEFT:
        return "left"
    elif key == K_SPACE:
        return "space"
    elif key == K_h:
        return "H"
    else:
        return ""


def draw(screen, character, nextCharacter,  position, score, seconds, coordinates):
    defaultFont = pygame.font.Font("SpaceMono-Regular.ttf", FONT_SIZE_SMALL)
    defaultFontGRANDE = pygame.font.Font("SpaceMono-Regular.ttf", FONT_SIZE_SMALL)

    ren1 = defaultFont.render("Score: " + str(score), 1, TEXT_COLOR)
    ren2 = defaultFont.render("Time: " + str(int(seconds)), 1, TIME_TEXT_COLOR if seconds < 15 else TEXT_COLOR)
    ren3 = MENU_FONT_SIZE_SMALL.render(character, 1, FONT_COLOR)
    ren4 = MENU_FONT_SIZE_SMALL.render(nextCharacter, 1, FONT_COLOR)
    bg = pygame.image.load ("bg.png")

    screen.blit(bg,(0,0))
    pygame.draw.line(screen, (20, 20, 20), (0, WIDTH - 65), (HEIGHT, WIDTH - 65), 5)

    i = 0
    while i < len(coordinates):
        screen.blit(defaultFontGRANDE.render(coordinates[i][0], 1, TEXT_COLOR), (coordinates[i][1], coordinates[i][2]))
        i += 1


    screen.blit(ren1, (HEIGHT - 120, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (position[0], position[1]))
    screen.blit(ren4, (centerText(ren4,"chica"), 10))


def menu(screen, seconds):

    color = (0,0,0)

    if int(seconds)%2==0:
        if color == (0,0,0):
            color = (255,100,100)
        else:
            color = (0,0,0)

    menu1= MENU_FONT_SIZE_BIG.render("Welcome to LETRIS", 1, (255,0,0))
    menu2= MENU_FONT_SIZE_SMALL.render("Press SPACE BAR to start", 1, color)

    screen.blit(menu1, (centerText(menu1, "grande"),30))
    screen.blit(menu2, (centerText(menu2,"grande"), WIDTH-150))


def menu2(screen, seconds, pos, menuActual):

    color = (255,100,100)
    menus = [
        ["Easy", (0,0,0), (95, 150)],
        ["Normal", (0,0,0), (95, 210)],
        ["Hard", (0,0,0), (95, 270)],
        ["Names", (0,0,0), (95, 330)],
        ["Records", (0,0,0), (95, 390)],
        ["Rules", (0,0,0), (95, 450)]
    ]

    titulo= MENU_FONT_SIZE_REGULAR.render("Select your game mode", 1, (255,0,0))

    pygame.draw.polygon(screen, color, [[45,pos+10],[80, pos+20],[45, pos+30]])

    menus[menuActual][1]=color

    menu1= MENU_FONT_SIZE_SMALL.render(menus[0][0], 1, menus[0][1])
    menu2= MENU_FONT_SIZE_SMALL.render(menus[1][0], 1, menus[1][1])
    menu3= MENU_FONT_SIZE_SMALL.render(menus[2][0], 1, menus[2][1])
    menu4= MENU_FONT_SIZE_SMALL.render(menus[3][0], 1, menus[3][1])
    menu5= MENU_FONT_SIZE_SMALL.render(menus[4][0], 1, menus[4][1])
    menu6= MENU_FONT_SIZE_SMALL.render(menus[5][0], 1, menus[5][1])

    screen.blit(titulo, (centerText(titulo, "grande"),30))
    screen.blit(menu1, menus[0][2])
    screen.blit(menu2, menus[1][2])
    screen.blit(menu3, menus[2][2])
    screen.blit(menu4, menus[3][2])
    screen.blit(menu5, menus[4][2])
    screen.blit(menu6, menus[5][2])


def showHelp(screen, palabraAyuda):
    if palabraAyuda=="":
        ren4 = MENU_FONT_SIZE_SMALL.render("Press H for help", 1, (255,0,0))
    else:
        ren4 = MENU_FONT_SIZE_SMALL.render(palabraAyuda, 1, (255,0,0))
    screen.blit(ren4, (centerText(ren4, "chica"), WIDTH-50))


