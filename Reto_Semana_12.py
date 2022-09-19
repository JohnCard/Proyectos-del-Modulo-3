from turtle import color
import matplotlib.pyplot as plt

print('''
      \n\t Sea usted bienvenido al programa donde le apoyaremos a crear una grafica de acuerdo a un determinado rango de años 😁,
      \n\t donde por cada año usted podrá introducir sus correspondientes ventas  📊 📈 📉 📄.
      ''')

print(f'\n Comenzemos a digitar el rango en el que va a trabajar.')
año_uno = input('Digite el año inicial: ')
while(año_uno.isnumeric() == False):
    año_uno = input(f'El dato digiatdo {año_uno} es invalido, favor de intentarlo de nuevo: ')
año_dos = input('Digite el año final del intervalo (el año final debe ser mayor al primero): ')
while(año_dos.isnumeric() == False):
    año_dos = input(f'El dato digiatdo {año_dos} es invalido, favor de intentarlo de nuevo: ')
# luego de que el usuario halla digitado los años con los que desea trabajar, esta condicional while la pondremos luego de eso para
# asegurarnos de que digite correctamente esos datos, asegurandonos de ninguno de ellos sea menor o igual a 0 o que el segundo que debe ser
# mayor al primero, sea efectivamente mayor
while(float(año_dos) <= float(año_uno) or float((año_uno and año_dos)) <= 0):
    print('\n\t ¡ Los 2 datos o alguno de ellos es incorrecto, favor de intentarlo de nuevo !')
    año_uno = input('Digite el año inicial: ')
    año_dos = input('Digite el año final del intervalo (el año final debe ser mayor al primero): ')
año_uno = float(año_uno)
año_dos = float(año_dos)

# inicializamos un contador con el valor del año_uno para que en el siguiente ciclo while, esta se va a ir aumentando de uno en uno hasta 
# superar al año_dos para irle agregando esos datos a la lista fixture que guardara todos esos años que valla iterando el contador    
contador = año_uno
lista_años = []
while contador <= (año_dos):
    # por cada iteración, la lista va a ir agregandose ese dato con .append()
    lista_años.append(contador)
    contador += 1

# ahora comenzaremos a recorrer la lista que acabamos de hacer para que por cada iteración que le mostremos al usuario en consola, 
# de acuerdo al año que se contemple, el digitará la cifra de ventas de ese correspondiente año, ademas de que inicializaremos una nueva 
# lista vacia, la cual va a ir almacenando por cada iteracion de este nuevo ciclo 
cifras_años = []
for año in lista_años:
    cifra = input(f'Digita la cifra correspondiente del año {año}: ')
    # en esta parte nos aseguraremos de que el usuario no digita nada que no tenga nada vque ver haha en ningun dato
    # durante el ciclo 🙅‍♂️:
    while(cifra.isnumeric() == False):
        cifra = input(f'El correspondiente dato digitado {cifra} no es valido, favor de intentarlo de nuevo: ')
    cifras_años.append(float(cifra))

# Es finalmente aqui donde detallamos como queremos que se vea nuestra grafica de datos linal.
# El eje de "x" se lo dedicamos al rango de años donde se registrara cada venta correspondiente a su año y para el eje "y"
# estará el rango disponible de ventas 
plt.plot(lista_años,cifras_años,color='g')
plt.title(f'Ventas del {año_uno} al {año_dos}')
plt.show() 
