#!/usr/bin/env python3

import math, os, random, sys

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *


def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # preparar la ventana
    pygame.display.set_caption("LETRIS 2017")

    screen = pygame.display.set_mode((ANCHO+400, ALTO))

    puntos = 0
    candidata = ""
    diccionario = []
    lectura(diccionario)
    letra = nuevaLetra()
    posicion = [0, 0]
    nuevaPosicion(posicion)
    mover=True
    siguienteLetra=""

    ayuda=False
    indiceAyuda=0
    palabraAyuda=""

    coordenadas=[]

    estaEnMenu = 0
    menuActual=0
    cursorY=150
    minLetras=0
    contador = 0
    penalizacion = 0

    while estaEnMenu==0:
        secs = (pygame.time.get_ticks() / 1000)
        screen.fill(COLOR_FONDO)
        menu(screen, secs)

        pygame.display.flip()


        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

            if e.type==KEYDOWN:
                if dameTeclaApretada(e.key) == "space":
                    estaEnMenu=1


    while estaEnMenu==1:

        secs = (pygame.time.get_ticks() / 1000)
        screen.fill(COLOR_FONDO)
        menu2(screen, secs,cursorY,menuActual)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

            if e.type == KEYDOWN:
                if dameTeclaApretada(e.key)=="up" and cursorY>150 and cursorY<=450:
                    cursorY-=60
                    menuActual-=1

                if dameTeclaApretada(e.key)=="down" and cursorY>=150 and cursorY<450:
                    cursorY+=60
                    menuActual+=1

                if e.type==KEYDOWN:
                    if dameTeclaApretada(e.key) == "space":
                        estaEnMenu=2


    screen = pygame.display.set_mode((ANCHO, ALTO))

# Tiempo total del juego
    gameClock = pygame.time.Clock()
    timeTicksInicial= pygame.time.get_ticks()
    totaltime = 0
    segundos = TIEMPO_MAX - penalizacion

    timeTicksTranscurrido= pygame.time.get_ticks() - timeTicksInicial
    segundos = TIEMPO_MAX - timeTicksTranscurrido / 1000 - penalizacion


    if menuActual==0:
        minLetras=0
        fps = 3
    elif menuActual==1:
        minLetras=1
        fps = 6
    elif menuActual==2:
        minLetras=4
        fps = 8

    while segundos > fps / 1000:

        if ayuda and palabraAyuda == "":
            palabraAyuda = darAyuda(menuActual, diccionario)

        if contador == 0 and not ayuda:
            siguienteLetra=nuevaLetra()
        elif ayuda and indiceAyuda != len(palabraAyuda):
            siguienteLetra=palabraAyuda[indiceAyuda]
        elif ayuda and indiceAyuda == len(palabraAyuda) and contador ==0:
            siguienteLetra=nuevaLetra()
        contador+=1

        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            # ver si se presiona alguna tecla
            if e.type == KEYDOWN and mover==True:
                direccion = dameTeclaApretada(e.key)
                moverLetra(posicion, direccion, coordenadas)

            if e.type == KEYDOWN:
                if dameTeclaApretada(e.key)=="H":
                    ayuda=True


        segundos = TIEMPO_MAX - pygame.time.get_ticks() / 1000 - float(penalizacion)

        bandera = actualizar(letra, posicion, coordenadas)

        if not bandera:
            if not ayuda :
                letra = siguienteLetra
                palabraAyuda = ""
                contador=0
            elif ayuda and indiceAyuda==len(palabraAyuda):
                palabraAyuda= ""
                indiceAyuda = 0
                letra = siguienteLetra
                ayuda=False
                contador=0
            else:
                letra = palabraAyuda[indiceAyuda]
                indiceAyuda+=1

            print(posicion)
            posicion=[0,0]
            nuevaPosicion(posicion)
            print("letras en pantalla",coordenadas)
            candidata = armarPalabra(coordenadas,diccionario)
            print("candidata",candidata)
            if candidata in diccionario and longitudMinima(candidata,minLetras):
                puntos += puntuar(candidata, diccionario)
            if menuActual==2:
                penalizacion += castigo(coordenadas)



        # limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        dibujar(screen, letra, siguienteLetra, posicion, puntos, segundos, coordenadas)
        if menuActual==0:
            mostrarAyuda(screen, palabraAyuda)
        pygame.display.flip()


    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()

