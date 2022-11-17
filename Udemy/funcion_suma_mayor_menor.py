def suma(lista):
    sum=0
    for x in range(len(lista)):
        sum=sum+lista[x]
    return sum

def mayor(lista):
    may=lista[0]
    for x in range(len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may

def menor(lista):
    men=lista[0]
    for x in range(len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men

listavalores=[]

d=int(input("¿Cuántos datos tendrá la lista?: "))
for k in range(d):
        listavalores.append(int(input("Introduce valor "+ str(k)+" en lista: ")))

print(listavalores)
print(suma(listavalores))
print(mayor(listavalores))
print( menor(listavalores))