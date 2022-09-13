import Reto_de_la_Semana_11_funciones 
from Reto_de_la_Semana_11_funciones import registrar_sql as registro, evaluar_listas as evaluacion, recorrer_cadena as recorrer,variables as cadenita

nombre_usuario = input('\n\t Haga usted el enorme favor de digitar su preciado y valiosisimo nombre, porfis 😁 (sin ascentos porfavor): ')
while(recorrer(nombre_usuario,cadenita) > 0):
    nombre_usuario = input(f'''\n Mi queridisimo y estimadisimo usuario, permitame informarle que su dato que que acaba de digitar ({nombre_usuario})
    no es para nada válido, favor de volver a intentarlo: ''')
answer = input(f'\n\t Le gustaría comenzar a registrar bases de datos basadas en formatos de lista señor/a {nombre_usuario} (Y/N)? ')
while(answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N'):
    answer = input(f'\t Mi queridisimo/a {nombre_usuario}, haga usted el enorme favor de digitar correctamente su respuesta, no sea malo 👺, (Y/N): ')

cont = 0
fixture = []

# Aqui inicializamos un ciclo while que no terminara hasta que el usuario se decida por terminarlo con algun caracter diferente de "y" o "Y"
while(answer == 'y' or answer == 'Y'):
    cont += 1
    '''Aqui llamamos a la función apodada como registro (registrar_sql) que se encargará de agregarle una nueva lista a fixture (registro(cont)) 
    con mas datos digitados por el usuario (tantos como el desee poner en la lista) '''
    fixture.append(registro(cont))
    answer = input(f'\n\t Le gustaría continuar digitando listas señor/a {nombre_usuario} (Y/N)? ')
    while(answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N'):
        answer = input('\t Haga usted el enorme favor de digitar correctamente su respuesta, no sea malo 👺, (Y/N): ')

# Esta nueva lista que estamos inicializando, va a guardar las listas modificadas sin datos repetidos de listas posteriores 
fixt_dos = []
''' Este dato lo inicializamos en -1 para que cuando el ciclo for de abajo inicie, al sumarle un 1 pase a ser 0 '''
cont_seg = -1

for i in fixture:
    fixt_dos.append([])
    '''
    Aqui ahora que el cont_seg vale 0 podremos empezar a leer los datos de la nueva lista que esta en la primer sentencia if por debajo de la
    intrucción "for u in i": 
    '''
    cont_seg += 1
    for u in i:
        ''' 
        Aqui al cont_seg  le sumamos otro 1 para que la condición solo evalue listas que efectivamente son posteriores a la iteración 
        actual yaque también se lo indicamos con los dos puntos despues del cont_seg+1 ":" para que lea los que son posteriores a él. 
        '''
        if(u in evaluacion(fixture[cont_seg+1:])):
            continue
        else: 
            fixt_dos[cont_seg].append(u)

# En esta instrucción mostraremos los elementos de la lista original
cont_tres = 0
print(f'\n\t Resultados de las listas originales digitadas por el señor/a {nombre_usuario}')
for i in fixture:
    cont_tres += 1
    print(f'\n Elemento numero {cont_tres} de la lista original: {i}')

# En esta instrucción mostraremos los elementos de la lista modificada
cont_cuarto = 0
print(f'\n\t Resultados de las listas modificadas para el señor/a {nombre_usuario}')
for i in fixt_dos:
    cont_cuarto += 1
    print(f'\n Elemento numero {cont_cuarto} de la lista modificada: {i}')
    
print('\n')
