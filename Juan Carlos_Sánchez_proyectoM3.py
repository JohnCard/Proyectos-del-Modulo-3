from turtle import title
import matplotlib.pyplot as plt
from random import randint as rand

# Esta será la lista la cual por el momento inicalizaremos con todos sus elementos en 0 por ahora, pero que 
# despues de que le asignemos el valor que le retorne la función contenedor_final en la lina 30, esta lista 
# (cajas[]) terminará con todos sus valores con distintas cifras asignadas para cada una 
# (ninguno mayo a 3000 o menor a 0), de manera totalmente aleatoria.
cajas = [0,0,0,0,0,0,0,0,0,0]
no_canicas = 3000

def contenedor_final(lista,num_canicas):
    '''
    Esta función realizará un ciclo while en base al num_canicas el cual mientras duré, va a realizar varios 
    ciclos for, y cada cilo for tiene la función de devolver una posición totalmente aleatoria del 1 al 9, y a 
    la posición que se haya escogido de manera aleatoria se le sumará un uno en la posición de la lista[] que 
    se le halla pasado como parametro.
    '''
    while num_canicas > 0:
        contenedores = [0,1,2,3,4,5,6,7,8,9]
        for i in range(9):
            # si el rand arroja un 1 lo tomaremos como izquierda "←" y si es 2 lo tomamos como derecha "→"
            si_no = rand(1,2)
            if si_no == 1:
                contenedores.pop()
            else:
                contenedores.pop(0)
        lista[contenedores[0]] += 1
        # aqui la condición para cual el no_canicas se va a ir reduciendo 
        num_canicas -= 1
    return lista

cajas = contenedor_final(cajas,no_canicas)

def cantidad_canicas(lista):
    '''
    esta función tomará como parametro una lista la cual con la variable canica va a recorrer, sin embargo, 
    aqui va a tomar como rango cada iteración de la lista para ser recorrido también, lo improtante es que lo 
    que retornará esta función será una lista con cada valor repetido la cantidad de veces que indique su 
    correspondiente iteración dentro de la lista
    '''
    frecuencias = []
    contador = 0
    for canica in lista:
        contador += 1
        for t in range(canica):
            frecuencias.append(contador)
    return frecuencias

# esta función será la que directamente creará el histograma y lo mostrará de a cuerdo con los parametros
# asignados por el usuario, parametros los cuales pueden resultar un tanto obvios por sus propios nombres desde
# un principio, pero aún asi los explicamos a continuación dentro de la función:
def create_grafico(lista,color,ec,title,xlabel,ylabel):
    '''
    1.- lista: que representará la lista que represente el histograma, donde la numeró de veces que se repita
    un valor en especifico en la lista, será la altura que tenga su barra de este mismo valor
    2.- color: que representará el color que lleve el histograma
    3.- ec: que representará el color con el que se valla a resaltar la linea que indique la separación de 
    cada grafico
    4.- title: que representará el encabezado indicando qué representa nuestro histograma
    5.- xlabel: que representará el nombre del eje "x"
    6.- ylabel: que representará el nombre del eje "y"
    '''
    plt.hist(lista,color=color,ec = ec)
    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel)
    plt.show()

create_grafico(cantidad_canicas(cajas),'b','black','Simulación de la Máquina de Galton','Distribución de canicas','Cantidad de canicas')