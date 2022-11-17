grupo=[{'cédula': '00014301503', 'nombre': 'Pepito', 'nota_fundamentos':4.3},
{'cédula': '1037678471', 'nombre': 'Fulanito', 'nota_fundamentos':3.2},
{'cédula': '71023567', 'nombre': 'Pancho', 'nota_fundamentos':5},
{'cédula': '32276123', 'nombre': 'Rita', 'nota_fundamentos':4.7},
{'cédula': '1036765245', 'nombre': 'Anita', 'nota_fundamentos':4.7},
{'cédula': '89122456', 'nombre': 'Pedrito', 'nota_fundamentos':4.7},
{'cédula': '289765345', 'nombre': 'Mat', 'nota_fundamentos':4.8},
{'cédula': '4576890', 'nombre': 'Dan', 'nota_fundamentos':4.8}]


sumanotas=0
notas=[]
for i in range(len(grupo)):
    notai=grupo[i]['nota_fundamentos']+sumanotas
    sumanotas=notai
promedio=sumanotas/len(grupo)

for i in range(len(grupo)):
    notas.append(grupo[i]['nota_fundamentos'])
notasi=list(dict.fromkeys(notas))

cuadro_honor={}

for i in range(1,4):
    cedulas=[]
    for j in range(len(grupo)):
        if grupo[j]['nota_fundamentos'] == max(notasi):
            cedulas.append(grupo[j]['cédula'])
    cuadro_honor[i]=cedulas
    notasi.remove(max(notasi))
lista=(promedio,cuadro_honor)
print(lista)