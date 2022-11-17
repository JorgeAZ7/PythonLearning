sueldo=int(input("Introduce el sueldo: "))
# condicional if
if sueldo>3000:
    print("El usuario debe pagar porcentaje en impuestos")
if sueldo<=3000:
    print("El usuario está excento de declarar renta")
if sueldo>6000 and sueldo <10000: # Operador lógico dos condiciones
    print("El usuario tiene que pagar bonificación de 1000")
if sueldo==20000 or sueldo==30000: #Cumplir solo una condicion
    print("El usuario paga un 10%")
