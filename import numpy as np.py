import numpy as np
import csv

cont = 0 

matriz_asiento = np.empty ([10,4], dtype='object')

matriz_datos_pasajeros = np.empty ([10,4], dtype='object')

mattriz_status_asiento = np.empty ([10,4], dtype='object')

with open ('datos.csv','w',newline="") as file:
    file.write ("Registro\n")

for i in range (10):
    for j in range (4):

        cont +=1

        matriz_asiento [i,j]= cont

print (matriz_asiento)        

for i in range (10):
    for j in range (4):

        matriz_datos_pasajeros[i,j] = "Sin datos"

for i in range (10):
    for j in range(4):
        mattriz_status_asiento [i,j] = "Vacio"

while (True):
    print ("MENU BUSES GOLONDRINA")
    print ("1.-Ingresar un pasajero")
    print ("2.-Ver nomina de pasajeros")
    print ("3.-Totalizar pasajeros")
    resp = 0
    while resp !=1 and resp !=2 and resp !=3: 
        try:
         resp = int(input("Ingrese una opcion: "))
         if resp !=1 and resp  and resp !=3:
             print ("Opcion inexistente, por favor, ingrese una valida") 
        except ValueError:
            print ("Caracter invalido. Intente otra vez")
            resp = 0


    if resp ==1:
        
        nomb = input("Ingrese el nombre del pasajero: ").upper()

        rut_pasajero = "111"
        while (len(rut_pasajero))<8 or (len(rut_pasajero))>9:
            try:
                rut_pasajero = input("Ingrese el rut el pasajero: ")
                if (len(rut_pasajero))<8 or (len(rut_pasajero))>9:
                    print ("rut inexistente, ingreselo nuevamente")
            except ValueError:
                print ("Error.Ingrese el rut el pasajero: ")
                rut_pasajero = 1


            
        edad_pasajero = int(input("Ingrese la edad del pasajero: "))
        asiento_pasajero = int(input("Ingrese el asiento del pasajero: "))        

        ocupado = 1

        while ocupado ==1:

            if asiento_pasajero not in matriz_asiento:
                asiento_pasajero = int(input("Asiento ocupado, por favor, elija otro: "))

            for i in range (10):
                    for j in range(4):

                        if matriz_asiento [i,j] == asiento_pasajero:
                            matriz_asiento [i,j] = "X"

                            dicc_pasajero ={"nombre":nomb,"edad":edad_pasajero,"rut": rut_pasajero,"sit":asiento_pasajero}
                            matriz_datos_pasajeros[i,j] = dicc_pasajero 

                            dato_pasajero = f"Nombre: {nomb}\t Rut: {rut_pasajero}\t Edad: {edad_pasajero} Asiento {asiento_pasajero}\n"

                            ocupado = 2  

        with open ('datos.csv','a', newline="") as file:
            file.write(dato_pasajero)   

        print (matriz_asiento)
        print (matriz_datos_pasajeros)    
        print (dato_pasajero)

    if resp ==2:

        for i in range (10):
            for j in range (4):
                if matriz_datos_pasajeros[i,j] != "Sin datos":
                    print (f"Nombre: {matriz_datos_pasajeros[i,j]['nombre']}\tRut: {matriz_datos_pasajeros[i,j]['rut']}\tEdad: {matriz_datos_pasajeros[i,j]['edad']}\tAsiento: {matriz_datos_pasajeros[i,j]['sit']} ")

    if resp == 3:
        con_pasajeros = 0
        for i in range (10):  
            for j in range (4):
                if matriz_asiento [i,j] == "X":

                    con_pasajeros +=1

        print (f"Cantidad de pasajeros: {con_pasajeros}") 
        print (f"Cantidad recaudada: {con_pasajeros*15000}")                       

        




        