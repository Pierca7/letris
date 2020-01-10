from configuracion import *
from principal import *
from extras import *
import math
import random


# Cargar en listaPalabras las palabras del archivo.
# Abre el archivo de texto como "diccionario", y cada palabra que contiene la agrega a una lista.
def lectura(listaPalabras):
    with open("diccionario.txt") as diccionario:
        for palabra in diccionario:
            listaPalabras.append(palabra.rstrip()) #.rstrip() elimina los \n
        diccionario.close() #Cierra el archivo
    return listaPalabras


# Puntua la palabra.
# Si la palabra recibida esta en el diccionario, evalua el puntaje de cada letra que la forma, y lo devuelve.
def puntuar(candidata, listaPalabras):
    vocales = "aeiou"
    dificiles = "jkqwxyz"
    puntaje=0

    if candidata in listaPalabras:
        for letra in candidata:
            if letra in vocales:
                puntaje+=1
            elif letra in dificiles:
                puntaje+=5
            else:
                puntaje+=2

    return puntaje


# Mueve la letra hacia la izquierda, derecha, o hacia abajo.
# Agrega las posiciones ocupadas en una matriz [posX, posY]. Evalua que tecla esta presionada y si la posicion
# que ocuparia al moverse no esta ocupada (no esta en la matriz) mueve la letra la cantidad de pixeles currespondiente a su tamano.
def moverLetra(posicion, direccion, coordenadas):

    if direccion=="down" and posicion[1]<490 and posicionLibre(posicion[0], posicion[1]+30, coordenadas):
        posicion[1]+=TAMANO_LETRA+10
    if direccion=="left" and posicion[0]>=TAMANO_LETRA and posicionLibre(posicion[0]-20, posicion[1], coordenadas):
        posicion[0]-=TAMANO_LETRA
    if direccion=="right" and posicion[0]<(ANCHO-20) and posicionLibre(posicion[0]+20, posicion[1], coordenadas):
        posicion[0]+=TAMANO_LETRA



# Devuelve una letra del abecedario al azar.
# Genera un entero aleatorio  y dependiendo de cual sea elige una letra al azar del grupo correspondiente.
# 10% de probabilidades de que la letra sea dificil, 50% de que sea consonante normal y 40% de que sea vocal.
def nuevaLetra():
    consonantes = "bcdfghlmnprstv"
    dificiles = "jkqwxyz"
    vocales = "aeiou"
    aleatorio = random.randint(1,10)

    if aleatorio == 1:
        letra = random.choice(dificiles)
    elif aleatorio >=2 and aleatorio <=6:
        letra = random.choice(consonantes)
    else:
        letra = random.choice(vocales)

    return letra


# Inventa una posicion. Por ejemplo: (x, y) x al azar e y bien arriba de
# la pantalla. La posicion en X estara dentro del rango (0, 380/TAMANO_LETRA) para que no salga la pantalla.

def nuevaPosicion(posicion):
    posicion[0] = TAMANO_LETRA * random.randint(0,(ANCHO-20)/TAMANO_LETRA)
    posicion[1] = TAMANO_LETRA*2
    return posicion


# Verifica que la ubicacion (posX, posY) no este ocupada (si esta en la matriz "coordenadas").
def posicionLibre(posX, posY, coordenadas):
    for elem in coordenadas:
        if [posX, posY] == [elem[1], elem[2]]:
            return False
    return True

# Opcional
# Recibe una matriz con las posiciones de cada letra y agraga las de la fila elegida (PosY)
def ordenarLetras(listaLetras, lista, fila ):
    for elem in lista:
        if elem[2]==fila:
            listaLetras.append(elem)
    listaLetras.sort(key=lambda pos: pos[1]) # Ordena la matriz de la fila elegida segun la posicion en X de cada letra.
    return listaLetras

# Arma la palabra que esta en la fila de la ultima letra que cayo. En
# esta funcion pueden usar las tres funciones opcionales.
def armarPalabra(coordenadas, listaPalabras):
    candidata=""
    palabra=[] #Matriz donde se agregan las letras consecutivas.
    filaOrdenada = []
    fila = coordenadas[-1][2] #Fila donde cayo la ultima letra.
    ordenarLetras(filaOrdenada, coordenadas, fila)

    for n in range(0,len(filaOrdenada)):

        #Si es la primera letra en la fila, la agrega directamente.
        if n==0:
            palabra.append(filaOrdenada[n])

        elif filaOrdenada[n][1] - filaOrdenada[n-1][1] == TAMANO_LETRA: #Evalua si las letras son consecutivas, de ser asi agrega la letra a la matriz.
                palabra.append(filaOrdenada[n])

        else:
            if coordenadas[-1] in palabra:              #Si las letras no son consecutivas, se que termina la palabra. Se evalua si la
                for elem in palabra:                                    #ultima letra que cayo esta dentro de la matriz formada. Si esta, con las letras de cada elemento
                    candidata+=elem[0]                                  #matriz forma la palabra y la devuelve.
                return candidata                                        #Si no esta, limpia la matriz y agrega la letra que se estaba evaluando
            else:
                palabra=[]
                palabra.append(filaOrdenada[n])

        if n==len(filaOrdenada)-1:                                      #Si la letra evaluada es la ultima de la fila, arma la palabra y la devuelve.
            for elem in palabra:
                candidata+=elem[0]
            return candidata

    return candidata


# Hace descender la letra, siempre que haya lugar hacia abajo. Devuelve
# True si la letra pudo bajar, y False en caso contrario. Si la letra no
# puede seguir bajando la guarda en letrasEnPantalla, y guarda su
# posicion en ocupados.

def actualizar(letra, posicion, coordenadas):

    if (posicion[1]+TAMANO_LETRA>500):                              #Si llega a la linea final, no baja mas y devuelve False.
        coordenadas.append([letra, posicion[0],posicion[1]])
        return False

    elif not posicionLibre(posicion[0],posicion[1]+TAMANO_LETRA+10, coordenadas):   #Si la siguiente posicion esta ocupada, no baja mas y devuelve False.
        coordenadas.append([letra, posicion[0],posicion[1]])
        return False

    else:
        posicion[1]+=TAMANO_LETRA+10                                 #Si la siguiente posicion no esta fuera de las permitidas y no esta ocupada, baja la cantidad de pixeles correspondientes al tamano de la letra.
        return True


def darAyuda(menuActual, diccionario):
    palabra = ""
    if menuActual==0:
        palabra = random.choice(diccionario)
    return palabra

def longitudMinima(palabra, cant):
    if len(palabra)>cant:
        return True
    return False

def castigo(coordenadas):
    fila = coordenadas[-1][2]
    filaOrdenada = []
    ordenarLetras(filaOrdenada, coordenadas, fila)
    if len(filaOrdenada)==(ANCHO/20):
        return 50
    return 0



