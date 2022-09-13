' Este será el modulo donde declaramos las funciones "def" necesarias para que el programa original funcione correctamente. '

def registrar_sql(cont,cont_seg = 0):
    ''' 
Esta función resivirá como parametro un cont el cual indica la iteración o el numero de la lista en la cuál se encuentran, inicializandose
también un cont_seg = 0 el cuál al iniciar cada una de sus iteraciones, estas van a mostrar ahora por cuál numero de dato va la correspondiente
lista en la que vallamos agregando datos
    '''
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
        answer = input(f'Desearía agregarle algún otro dato para la lista numero {cont} (Y/N)? ')
        while(answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N'):
            answer = input('\t Haga usted el enorme favor de digitar correctamente su respuesta, no sea malo "👺", (Y/N): ')
    return fixture

def evaluar_listas(list_complete):
    '''
    Esta función vuscará retornar una lista la cual muestre solo los arreglos que se necesiten para determinada ocasión en el caso del 
    modulo del "Reto_semanal_uno.py".
    '''
    fixture = []
    for i in list_complete:
        for t in i:
            fixture.append(t)
    return fixture

# Esta variable va a contener solo aquellos valores requeridos para cuando preguntemos el nombre de un usuario
variables = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

def recorrer_cadena(cadena,cadena_dos):
    '''
    Esta función primero va a recibir como parametro la cadena de la derecha, la cual va a recorrer para leer cada uno de sus caracteres y 
    revisar con el "not in" si es uno solo de ellos no llegase a existir en la cadena de caracteres que si es válida (cadena_dos), el parametro
    "cadena_dos" se le pasa como parametro los caracteres que se requieren comparar para asegurarse de que el usuario esta digitando bien
    los valores solicitados
    '''
    cont = 0
    for i in cadena:
        if(i not in cadena_dos):
            cont += 1
    return cont