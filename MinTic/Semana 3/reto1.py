print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
nombre=input("Por favor ingrese su nombre: ")
materia=input("Ingrese el nombre de la materia: ")
porcentaje=0
nota_acumulada=0
decision='S'
i=1
while porcentaje != 100 and decision=='S':
    notai=float(input("Ingrese la nota obtenida: "))
    porcentajei=float(input("Ingrese el procentaje de la nota: "))
    porcentaje=porcentaje+porcentajei
    nota_acumulada=nota_acumulada+notai*porcentajei/100
    if porcentaje<100:
        decision=input("¿Falta añadir notas? S/N ")
    elif porcentaje>100:
        print("El porcentaje evaluado de una materia no puede ser mayor a 100")
        porcentaje=porcentaje-porcentajei
        nota_acumulada=nota_acumulada-notai*porcentajei/100
if nota_acumulada>=3:
    resultado='Aprobado'
elif nota_acumulada<3:
    resultado='Reprobado'
print("El estudiante ",nombre," cursó la materia ",materia," y obtuvo ",nota_acumulada," resultando en ",resultado)