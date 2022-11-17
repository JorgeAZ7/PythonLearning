def conversacion(mensaje):
    print('Hola')
    print('¿Cómo estás?')
    print(mensaje)
    print('Adios')

opcion=int(input('Elige una opción (1, 2, 3): '))
if opcion==1:
    conversacion('Elegiste la opción uno')
elif opcion==2:
    conversacion('Elegiste la opción dos')
elif opcion==3:
    conversacion('Elegiste la opción dos')
else:
    print('Escribe la opción corrrecta')


