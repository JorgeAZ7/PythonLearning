grupo1=[{'cédula': '00014301503', 'nombre': 'Pepito', 'nota_fundamentos':4.3},
{'cédula': '1037678471', 'nombre': 'Fulanito', 'nota_fundamentos':3.2},
{'cédula': '71023567', 'nombre': 'Pancho', 'nota_fundamentos':5},
{'cédula': '32276123', 'nombre': 'Rita', 'nota_fundamentos':4.7},
{'cédula': '1036765245', 'nombre': 'Anita', 'nota_fundamentos':4.7},
{'cédula': '89122456', 'nombre': 'Pedrito', 'nota_fundamentos':4.7},
{'cédula': '289765345', 'nombre': 'Mat', 'nota_fundamentos':4.8},
{'cédula': '4576890', 'nombre': 'Dan', 'nota_fundamentos':4.8}]

grupo2=[{'cédula': '00032145678', 'nombre': 'Valen', 'nota_fundamentos':3},
{'cédula': '1067678654', 'nombre': 'Cris', 'nota_fundamentos':4.5},
{'cédula': '45677890', 'nombre': 'John', 'nota_fundamentos':4.5},
{'cédula': '72033405', 'nombre': 'Carmen', 'nota_fundamentos':4.5},
{'cédula': '1036765245', 'nombre': 'Jordan', 'nota_fundamentos':4.5},
{'cédula': '89122456', 'nombre': 'Pedro', 'nota_fundamentos':2.3},
{'cédula': '289765345', 'nombre': 'Camilo', 'nota_fundamentos':3.7}]

def calcular_promedio_y_cuadro_honor(grupo):
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
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
        
    #ACÁ TERMINA LA FUNCIÓN SOLUCIÓN
    return promedio, cuadro_honor

calcular_promedio_y_cuadro_honor(grupo1)
calcular_promedio_y_cuadro_honor(grupo2)   
"""
¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE! ¡IMPORTANTE!
NO AÑADIR CÓDIGO FUERA DE LA FUNCIÓN calcular_promedio_y_cuadro_honor(grupo) .
SOLO AÑADIR CÓDIGO ENTRE EL ESPACIO DONDE DICE: ACÁ INICIA... ACÁ TERMINA
"""