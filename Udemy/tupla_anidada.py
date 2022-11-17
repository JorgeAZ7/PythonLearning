def cargar_paisespoblacion():
    paises=[]
    cpaises=int(input("Define cantidad de países: "))
    for x in range(cpaises):
        nom=input("Ingresar el nombre del país: ")
        cant=int(input("Ingrese la cantidad de habitantes: "))
        paises.append((nom,cant))
    return paises

def imprimir(paises):
    print("Paises y población:")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])

def pais_maspoblacion(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Paises con mas población: ", paises[pos][0])

paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)
