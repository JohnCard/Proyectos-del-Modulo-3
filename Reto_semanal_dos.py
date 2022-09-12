' Este será el modulo donde declaramos las funciones "def" necesarias para que el programa original funcione correctamente. '

''' 
Esta función resivirá como parametro un cont el cual indica la iteración o el numero de la lista en la cuál se encuentran, inicializandose
también un cont_seg = 0 el cuál al iniciar cada una de sus iteraciones, estas van a mostrar ahora por cuál numero de dato va la correspondiente
lista en la que vallamos agregando datos
'''
import string

def registrar_sql(cont,cont_seg = 0):
    print(f'\n Comenzemos con la lista numero {cont}.')
    answer = 'y'
    fixture = []
    while(answer == 'y' or answer == 'Y'):
        '''
        Aqui es donde realmente se podrá contemplar como el cont_seg empieza a aumentar de uno en uno durante este ciclo while, mientras el 
        usuario continue digitando datos a la lista
        '''
        cont_seg += 1
        # Y es justo en esta parte donde mostramos la iteración por la que va nuestro dato {cont_seg}
        fixture.append(input(f'Ingrese el dato numero {cont_seg} de la lista numero {cont}: '))
        answer = input(f'Desea ingresarle algún otro dato a la lista numero {cont} (Y/N)? ')
        while(answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N'):
            answer = input('\t Haga usted el enorme favor de digitar correctamente su respuesta, no sea malo "👺", (Y/N): ')
    return fixture

def evaluar_listas(list_complete):
    fixture = []
    for i in list_complete:
        for t in i:
            fixture.append(t)
    return fixture

variables = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

def recorrer_cadena(cadena,cadena_dos):
    cont = 0
    for i in cadena:
        if(i not in cadena_dos):
            cont += 1
    return cont