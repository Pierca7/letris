import pygame
from pygame.locals import *
from configuracion import *

def centrarTexto(texto, ventana):
    text_rec= texto.get_rect()
    if ventana == "chica":
        posX= (ANCHO-text_rec[2]) /2
        return posX
    if ventana == "grande":
        posX= (ANCHO+400-text_rec[2]) /2
        return posX

def dameTeclaApretada(key):
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


def dibujar(screen, letra,siguienteLetra,  posicion, puntos, segundos,coordenadas):
    defaultFont = pygame.font.Font("SpaceMono-Regular.ttf", TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font("SpaceMono-Regular.ttf", TAMANO_LETRA_GRANDE)

    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL if segundos < 15 else COLOR_TEXTO)
    ren3 = MENU_FONT.render(letra, 1, COLOR_LETRA)
    ren4 = MENU_FONT.render(siguienteLetra, 1, COLOR_LETRA)
    bg = pygame.image.load ("bg.png")

    screen.blit(bg,(0,0))
    pygame.draw.line(screen, (20, 20, 20), (0, ALTO - 65), (ANCHO, ALTO - 65), 5)

    i = 0
    while i < len(coordenadas):
        screen.blit(defaultFontGRANDE.render(coordenadas[i][0], 1, COLOR_TEXTO), (coordenadas[i][1], coordenadas[i][2]))
        i += 1


    screen.blit(ren1, (ANCHO - 120, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (posicion[0], posicion[1]))
    screen.blit(ren4, (centrarTexto(ren4,"chica"), 10))


def menu(pantalla, segundos):

    color = (0,0,0)

    if int(segundos)%2==0:
        if color == (0,0,0):
            color = (255,100,100)
        else:
            color = (0,0,0)

    menu1= MENU_FONT_GRANDE.render("Bienvenido al LETRIS", 1, (255,0,0))
    menu2= MENU_FONT.render("Pulsa BARRA ESPACIADORA para empezar", 1, color)

    pantalla.blit(menu1, (centrarTexto(menu1, "grande"),30))
    pantalla.blit(menu2, (centrarTexto(menu2,"grande"), ALTO-150))


def menu2(pantalla, segundos, pos, menuActual):

    color = (255,100,100)
    menus = [["Facil", (0,0,0),(95, 150)],["Normal",(0,0,0),(95, 210)],["Dificil", (0,0,0),(95, 270)],["Nombres", (0,0,0),(95, 330)],["Records", (0,0,0),(95, 390)],["Reglas",(0,0,0),(95, 450)]]

    titulo= MENU_FONT_MEDIO.render("Elija el modo de juego", 1, (255,0,0))

    pygame.draw.polygon(pantalla, color, [[45,pos+10],[80, pos+20],[45, pos+30]])

    menus[menuActual][1]=color

    menu1= MENU_FONT.render(menus[0][0], 1, menus[0][1])
    menu2= MENU_FONT.render(menus[1][0], 1, menus[1][1])
    menu3= MENU_FONT.render(menus[2][0], 1, menus[2][1])
    menu4= MENU_FONT.render(menus[3][0], 1, menus[3][1])
    menu5= MENU_FONT.render(menus[4][0], 1, menus[4][1])
    menu6= MENU_FONT.render(menus[5][0], 1, menus[5][1])

    pantalla.blit(titulo, (centrarTexto(titulo, "grande"),30))
    pantalla.blit(menu1, menus[0][2])
    pantalla.blit(menu2, menus[1][2])
    pantalla.blit(menu3, menus[2][2])
    pantalla.blit(menu4, menus[3][2])
    pantalla.blit(menu5, menus[4][2])
    pantalla.blit(menu6, menus[5][2])


def mostrarAyuda(pantalla, palabraAyuda):
    if palabraAyuda=="":
        ren4 = MENU_FONT.render("Pulsa H para la AYUDA", 1, (255,0,0))
    else:
        ren4 = MENU_FONT.render(palabraAyuda, 1, (255,0,0))
    pantalla.blit(ren4, (centrarTexto(ren4, "chica"), ALTO-50))


