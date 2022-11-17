nota1=int(input("Introduce nota 1: "))
nota2=int(input("Introduce nota 2: "))
nota3=int(input("Introduce nota 3: "))
prom=(nota1+nota2+nota3)/3
if prom>=7:
    print("Promocionado")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Reprobado")
