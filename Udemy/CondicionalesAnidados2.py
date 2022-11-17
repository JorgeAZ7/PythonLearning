nota1=int(input("Introduce nota 1: "))
nota2=int(input("Introduce nota 2: "))
nota3=int(input("Introduce nota 3: "))
media=(nota1+nota2+nota3)/3

if media == 9 or media == 10:
    print("Sobresaliente")
elif media == 5:
    print("Suficiente")
elif media == 6:
    print("Regular")
elif media == 7 or media == 8:
    print("Bien")
else:
    print("Insuficiente")
