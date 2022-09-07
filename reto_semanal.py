'''
def crear_listados(): ---

def eliminar_dup(): ---
'''

'''
● Que permita crear dos listas de distintas longitudes.
● Que la longitud y los elementos de cada lista sean especificados por el usuario.
● Que imprima las listas indicando que son las listas originales.
● Que elimine de la primera lista los nombres de la segunda.
● Que imprima la primera lista indicando que se han eliminado los elementos que estaban también en la segunda.

Como un pequeño consejo, si empleas dos funciones, una para crear las listas y otra para eliminar los duplicados, se te facilitará el proceso.
'''

def crear_listados(nombre,lista):
    '''
    Esta funcionalidad la integramos para que sea ella quien se haga cargo de que de acuerdo al nombre que se le entregue como parametro,
    al otro parametro que se le otorgue como la lista de interes, será a la que le pasará los nombres que se le agreguen por defecto
    ''' 
    if nombre == '':
        nombre = 'Nombre indefinido'
    else:
        lista.append(nombre)
    return lista

def eliminar_duplicados(lista_uno,lista_dos,lista_tres):
    for i in lista_uno:
        if i not in lista_dos:
            lista_tres.append(i)
        else:
            pass
    return lista_tres

fixture_nombres = [] 
fixture_nombres_modificado = []
fixture_nombres_dos = []

print(' \n \t Empezaremos con la 1ra lista de nuestro programa. ')
answer = 'T'
while answer == 'T':
    nombre = input('\n Digite un nuevo nombre para la lista de nombres: ')
    fixture_nombres.append(nombre)
    answer = input('\n Desearía digitar algún otro nombre? (T/N): ')

print(' \n \t Ahora vamos a proseguir con la segunda lista de nombres para nuestro programa. ')
answer_dos = 'T'
while answer_dos == 'T':
    nomb = input('\n Digite un nuevo nombre para la lista de nombres: ')
    fixture_nombres_dos = crear_listados(nomb,fixture_nombres_dos)
    answer_dos = input('\n Desearía digitar algún otro nombre? (T/N): ')
    
fixture_nombres_modificado = eliminar_duplicados(fixture_nombres,fixture_nombres_dos,fixture_nombres_modificado)    
    
print(f'''
Número 1:
{fixture_nombres}

Número 2:
{fixture_nombres_dos}

Modificada y Final:
{fixture_nombres_modificado}
      ''')