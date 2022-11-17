from multiprocessing.managers import ValueProxy


def funcion_practica2(x): #Esa función definirá el descuento de una variable
    valor=x*0.9
    return valor

x=int(input('Definir un valor x: '))
funcion_practica2(x)
print('El precio ',x,' con un 10 por ciento de descuento es ', valor)