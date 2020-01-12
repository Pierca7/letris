import math
import random

from configuration import *
from main import *
from extras import *

def readDictionary(words):
    with open("dictionary.txt") as dictionary:
        for word in dictionary:
            words.append(word.rstrip()) 
        dictionary.close() 
    return words


def givePunctuation(word, words):
    vowels = "aeiou"
    hardOnes = "jkqwxyz"
    punctuation = 0

    if word in words:
        for character in word:
            if character in vowels:
                punctuation+=1
            elif character in hardOnes:
                punctuation+=5
            else:
                punctuation+=2

    return punctuation


def moveCharacter(position, direction, coordinates):
    if direction=="down" and position[1]<490 and positionIsFree(position[0], position[1]+30, coordinates):
        position[1]+=FONT_SIZE_SMALL+10
    if direction=="left" and position[0]>=FONT_SIZE_SMALL and positionIsFree(position[0]-20, position[1], coordinates):
        position[0]-=FONT_SIZE_SMALL
    if direction=="right" and position[0]<(HEIGHT-20) and positionIsFree(position[0]+20, position[1], coordinates):
        position[0]+=FONT_SIZE_SMALL



def newCharacter():
    consonants = "bcdfghlmnprstv"
    hardOnes = "jkqwxyz"
    vowels = "aeiou"
    randomNumber = random.randint(1,10)

    if randomNumber == 1:
        character = random.choice(hardOnes)
    elif randomNumber >=2 and randomNumber <=6:
        character = random.choice(consonants)
    else:
        character = random.choice(vowels)

    return character


def newPosition(position):
    position[0] = FONT_SIZE_SMALL * random.randint(0,(HEIGHT-20)/FONT_SIZE_SMALL)
    position[1] = FONT_SIZE_SMALL*2

    return position


def positionIsFree(posX, posY, coordinates):
    for elem in coordinates:
        if [posX, posY] == [elem[1], elem[2]]:
            return False
    return True


def sortCharacters(words, list, row):
    for elem in list:
        if elem[2] == row:
            words.append(elem)
    words.sort(key=lambda pos: pos[1])
    return words


def buildWord(coordinates, words):
    candidate = ""
    word = [] 
    sortedRow = []
    row = coordinates[-1][2] 
    sortCharacters(sortedRow, coordinates, row)

    for n in range(0,len(sortedRow)):

        if n==0:
            word.append(sortedRow[n])

        elif sortedRow[n][1] - sortedRow[n-1][1] == FONT_SIZE_SMALL: 
                word.append(sortedRow[n])

        else:
            if coordinates[-1] in word:              
                for elem in word:                                    
                    candidate+=elem[0]                                  
                return candidate                                        
            else:
                word=[]
                word.append(sortedRow[n])

        if n==len(sortedRow)-1:                                      
            for elem in word:
                candidate+=elem[0]
            return candidate

    return candidate


def refresh(character, position, coordinates):

    if (position[1] + FONT_SIZE_SMALL > 500):                              
        coordinates.append([character, position[0], position[1]])
        return False

    elif not positionIsFree(position[0], position[1] + FONT_SIZE_SMALL + 10, coordinates):   
        coordinates.append([character, position[0], position[1]])
        return False

    else:
        position[1]+=FONT_SIZE_SMALL+10
        return True


def giveHelp(currentMenuItem, dictionary):
    word = ""
    if currentMenuItem == 0:
        word = random.choice(dictionary)
    return word

def minLength(word, length):
    return len(word) > length

def penalize(coordinates):
    row = coordinates[-1][2]
    sortedRow = []
    sortCharacters(sortedRow, coordinates, row)
    if len(sortedRow)==(HEIGHT/20):
        return 50
    return 0



