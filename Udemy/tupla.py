def cargar_fecha():
    dd=int(input("Ingrese número del día: "))
    mm=int(input("Ingrese número del mes: "))
    aa=int(input("Ingrese número del año: "))
    tupla= (dd,mm,aa)
    return tupla

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

fecha=cargar_fecha()
imprimir_fecha(fecha)
