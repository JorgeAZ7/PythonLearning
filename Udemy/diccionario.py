def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano: ")
        ing=input("Ingrese palabra en inglés: ")
        diccionario[caste]=ing
        continua=input("¿Quiere cargar otra palabra?: [S/N]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])

def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en castellano a consultar: ")
    if pal in diccionario:
        print("En ingles significa: ",diccionario[pal])

#Bloque principal
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)