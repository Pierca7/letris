#!/usr/bin/env python3

import math, os, random, sys
import pygame

from pygame.locals import *
from configuration import *
from functions import *
from extras import *


def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    pygame.display.set_caption("LETRIS 2017")

    screen = pygame.display.set_mode((HEIGHT+400, WIDTH))

    points = 0
    candidate = ""
    dictionary = []
    readDictionary(dictionary)
    character = newCharacter()
    position = [0, 0]
    newPosition(position)
    move=True
    nextCharacter=""

    helpEnabled=False
    helpIndex=0
    helpWord=""

    coordinates=[]

    isInMenu = 0
    currentMenuItem=0
    cursorY=150
    minCharacters=0
    counter = 0
    penalization = 0

    while isInMenu==0:
        secs = (pygame.time.get_ticks() / 1000)
        screen.fill(BACKGROUND_COLOR)
        menu(screen, secs)

        pygame.display.flip()


        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

            if e.type==KEYDOWN:
                if getPressedKey(e.key) == "space":
                    isInMenu=1


    while isInMenu==1:

        secs = (pygame.time.get_ticks() / 1000)
        screen.fill(BACKGROUND_COLOR)
        menu2(screen, secs,cursorY,currentMenuItem)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

            if e.type == KEYDOWN:
                if getPressedKey(e.key)=="up" and cursorY>150 and cursorY<=450:
                    cursorY-=60
                    currentMenuItem-=1

                if getPressedKey(e.key)=="down" and cursorY>=150 and cursorY<450:
                    cursorY+=60
                    currentMenuItem+=1

                if e.type==KEYDOWN:
                    if getPressedKey(e.key) == "space":
                        isInMenu=2


    screen = pygame.display.set_mode((HEIGHT, WIDTH))

    gameClock = pygame.time.Clock()
    timeTicksInicial= pygame.time.get_ticks()
    totaltime = 0
    seconds = MAX_TIME - penalization

    timeTicksTranscurrido= pygame.time.get_ticks() - timeTicksInicial
    seconds = MAX_TIME - timeTicksTranscurrido / 1000 - penalization


    if currentMenuItem==0:
        minCharacters=0
        fps = 3
    elif currentMenuItem==1:
        minCharacters=1
        fps = 6
    elif currentMenuItem==2:
        minCharacters=4
        fps = 8

    while seconds > fps / 1000:

        if helpEnabled and helpWord == "":
            helpWord = giveHelp(currentMenuItem, dictionary)

        if counter == 0 and not helpEnabled:
            nextCharacter=newCharacter()
        elif helpEnabled and helpIndex != len(helpWord):
            nextCharacter=helpWord[helpIndex]
        elif helpEnabled and helpIndex == len(helpWord) and counter ==0:
            nextCharacter=newCharacter()
        counter+=1

        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN and move==True:
                direccion = getPressedKey(e.key)
                moveCharacter(position, direccion, coordinates)

            if e.type == KEYDOWN:
                if getPressedKey(e.key)=="H":
                    helpEnabled=True


        seconds = MAX_TIME - pygame.time.get_ticks() / 1000 - float(penalization)

        flag = refresh(character, position, coordinates)

        if not flag:
            if not helpEnabled :
                character = nextCharacter
                helpWord = ""
                counter=0
            elif helpEnabled and helpIndex==len(helpWord):
                helpWord= ""
                helpIndex = 0
                character = nextCharacter
                helpEnabled=False
                counter=0
            else:
                character = helpWord[helpIndex]
                helpIndex+=1

            print(position)
            position=[0,0]
            newPosition(position)
            candidate = buildWord(coordinates,dictionary)
            if candidate in dictionary and minLength(candidate,minCharacters):
                points += givePunctuation(candidate, dictionary)
            if currentMenuItem==2:
                penalization += penalize(coordinates)

        screen.fill(BACKGROUND_COLOR)

        draw(screen, character, nextCharacter, position, points, seconds, coordinates)
        if currentMenuItem==0:
            showHelp(screen, helpWord)
        pygame.display.flip()


    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()

