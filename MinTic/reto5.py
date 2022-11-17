def clima():
    import csv
    import json
    with open("data.csv","r") as archivo:
        datos=csv.reader(archivo)
        encabezado = next(datos)
        id=[]
        location=[]
        temperature=[]
        pressure=[]

    temperature_list_1=[]
    temperature_list_2=[]
    temperature_list_3=[]
    temperature_list_4=[]
    temperature_list_5=[]

    pressure_list_1=[]
    pressure_list_2=[]
    pressure_list_3=[]
    pressure_list_4=[]
    pressure_list_5=[]

    for fila in datos:
        id.append(fila[0])
        location.append(fila[1])
        temperature.append(float(fila[2]))
        pressure.append(float(fila[3]))

    for i in range(len(location)):
        if location[i] == '1':
            temperature_list_1.append(temperature[i])
            pressure_list_1.append(pressure[i])
        elif location[i] == '2':
            temperature_list_2.append(temperature[i])
            pressure_list_2.append(pressure[i])
        elif location[i] == '3':
            temperature_list_3.append(temperature[i])
            pressure_list_3.append(pressure[i])
        elif location[i] == '4':
            temperature_list_4.append(temperature[i])
            pressure_list_4.append(pressure[i])
        elif location[i] == '5':
            temperature_list_5.append(temperature[i])
            pressure_list_5.append(pressure[i])
    
    av_temperature_1=round(sum(temperature_list_1)/len(temperature_list_1),1)
    av_pressure_1=round(sum(pressure_list_1)/len(pressure_list_1),1)
    
    av_temperature_2=round(sum(temperature_list_2)/len(temperature_list_2),1)
    av_pressure_2=round(sum(pressure_list_2)/len(pressure_list_2),1)
    
    av_temperature_3=round(sum(temperature_list_3)/len(temperature_list_3),1)
    av_pressure_3=round(sum(pressure_list_3)/len(pressure_list_3),1)
    
    av_temperature_4=round(sum(temperature_list_4)/len(temperature_list_4),1)
    av_pressure_4=round(sum(pressure_list_4)/len(pressure_list_4),1)
    
    av_temperature_5=round(sum(temperature_list_5)/len(temperature_list_5),1)
    av_pressure_5=round(sum(pressure_list_5)/len(pressure_list_5),1)
    
    
    av_temperaturelist=[]
    av_pressurelist=[]
    
    for i in range(len(location)):
        if location[i] == '1':
            if temperature[i]>av_temperature_1:
                av_temperaturelist.append('SI')
            elif temperature[i]<av_temperature_1:
                av_temperaturelist.append('NO')
            elif temperature[i] == av_temperature_1:
                av_temperaturelist.append('IGUAL')
        
            if pressure[i]>av_pressure_1:
                av_pressurelist.append('SI')
            elif pressure[i]<av_pressure_1:
                av_pressurelist.append('NO')
            elif pressure[i] == av_pressure_1:
                av_pressurelist.append('IGUAL')
        
        elif location[i] == '2':
            if temperature[i]>av_temperature_2:
                av_temperaturelist.append('SI')
            elif temperature[i]<av_temperature_2:
                av_temperaturelist.append('NO')
            elif temperature[i] == av_temperature_2:
                av_temperaturelist.append('IGUAL')

            if pressure[i]>av_pressure_2:
                av_pressurelist.append('SI')
            elif pressure[i]<av_pressure_2:
                av_pressurelist.append('NO')
            elif pressure[i] == av_pressure_2:
                av_pressurelist.append('IGUAL')

        elif location[i] == '3':
            if temperature[i]>av_temperature_3:
                av_temperaturelist.append('SI')
            elif temperature[i]<av_temperature_3:
                av_temperaturelist.append('NO')
            elif temperature[i] == av_temperature_3:
                av_temperaturelist.append('IGUAL')

            if pressure[i]>av_pressure_3:
                av_pressurelist.append('SI')
            elif pressure[i]<av_pressure_3:
                av_pressurelist.append('NO')
            elif pressure[i] == av_pressure_3:
                av_pressurelist.append('IGUAL')

        elif location[i] == '4':
            if temperature[i]>av_temperature_4:
                av_temperaturelist.append('SI')
            elif temperature[i]<av_temperature_4:
                av_temperaturelist.append('NO')
            elif temperature[i] == av_temperature_4:
                av_temperaturelist.append('IGUAL')

            if pressure[i]>av_pressure_4:
                av_pressurelist.append('SI')
            elif pressure[i]<av_pressure_4:
                av_pressurelist.append('NO')
            elif pressure[i] == av_pressure_4:
                av_pressurelist.append('IGUAL')

        elif location[i] == '5':
            if temperature[i]>av_temperature_5:
                av_temperaturelist.append('SI')
            elif temperature[i]<av_temperature_5:
                av_temperaturelist.append('NO')
            elif temperature[i] == av_temperature_5:
                av_temperaturelist.append('IGUAL')

            if pressure[i]>av_pressure_5:
                av_pressurelist.append('SI')
            elif pressure[i]<av_pressure_5:
                av_pressurelist.append('NO')
            elif pressure[i] == av_pressure_5:
                av_pressurelist.append('IGUAL')

    data_list=[]
    header=['id','location','temperature','pressure','above_avg_temp','above_avg_pres']

    for i in range(len(id)):
        data_list.append([id[i],location[i],temperature[i],pressure[i],av_temperaturelist[i],av_pressurelist[i]])


    with open('data_nuevo.csv','w') as csvfile:
        escritor=csv.writer(csvfile)
        escritor.writerow(header)
        for i in range(len(id)):
            escritor.writerow(data_list[i])
            
    return datos

clima()