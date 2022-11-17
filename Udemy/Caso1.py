print("Datos de la empresa")


nombre1=input("Ingrese nombre del producto: ")
precio1=int(input("Ingrese precio del producto: "))
nombre2=input("Ingrese nombre del producto: ")
precio2=int(input( "Ingrese precio del producto: "))

# Constante:
BONIFICACION = 20

# """"OPERADORES COMILLAS ES PARA PONER COMENTARIOS MÁS LARGOS DE UNA LÍNEA"""
# PARA COMENTARIOS DE UNA LÍNEA SE UTILIZA #

precio_compra_total = precio1 + precio2
comparar = precio1>=precio2 #operador comparación
logico = (precio1 < precio2 and precio1==precio2) #Operador lógico


cabecera="Resultados del producto {0} y del producto {1}"
#Concatenar
print(cabecera.format(nombre1, nombre2))
print("¿El precio del primer valor es mayor o igual al precio del segundo valor?:")
print(comparar)
print("La suma de los dos productos es: " + str(precio_compra_total))
print("precio1<precio2 and precio1 == precio2")
print(logico)
precio_compra_total += BONIFICACION
print("Al precio total le incrementamos su valor que tiene la constante: " +str(precio_compra_total))