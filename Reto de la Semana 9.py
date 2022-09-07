import string
def alfabeto_letra(letra):
    ubicacion = string.ascii_lowercase.index(letra.lower())
    print(f'''
La letra que va despues de {letra.lower()} en el alfabeto es: {string.ascii_lowercase[ubicacion + 1]}
La letra que va antes de {letra.lower()} en el alfabeto es: {string.ascii_lowercase[ubicacion - 1]}
    ''')

answer = 'y'
while answer == 'y' or answer == 'Y':
    letra = input('Digite su correspondiente letra: ')
    while(letra.isalpha() == False or len(letra) > 1):
        letra = input('Digite la letra de nuevo: ')
    alfabeto_letra(letra)
    answer = input('Desea volver a intentarlo? ')
