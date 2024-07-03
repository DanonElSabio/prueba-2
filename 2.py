import numpy as np
import csv 
import funciones_buses as fb
cont = 0

matriz_asientos = np.empty ([10,4],dtype='object')

matriz_datos_clientes = np.empty ([10,4], dtype='object')



for i in range (10):
    for j in range (4):
        cont+=1
        matriz_asientos[i,j]=cont

for i in range (10):
    for j in range (4):
        dicc_datos_pasajero= {"nombre":'sin datos',"rut":'sin datos',"edad":'sin datos',"sit":"sin datos"}
        matriz_datos_clientes[i,j]= "sin datos"

with open ('datos.csv','w',newline='') as file:
    file.write ("Resgistro\n")

with open ('log.txt','w') as archivo:
    archivo.write ("Reagistro pasajeros:\n")




while (True):
    print (matriz_asientos)
    print ("MENU")
    print ("1.-Ingresar un pasajero")
    print ("2.-Ver listado de pasajeros")
    print ("3.-Totalizar bus")
    print ("4.- Buscar un pasajero")
    print ("5.- Salir")
    resp=0
    while resp!=1 and resp !=2 and resp !=3 and resp !=4 and resp !=5:
        try:
            resp = int(input("Ingrese una opción: "))
            if resp!=1 and resp !=2 and resp !=3 and resp !=4 and resp !=5:
                print ("Opcion no valida, por favor, ingrese una existente")
        except ValueError:
            print ("Caracter invalido, por favor, ingrese uno valido")  
    
    if resp ==1:

        fb.ingresar_pasajero (matriz_asientos,matriz_datos_clientes)

        
    if resp == 2:

        fb.mostra_listado (matriz_datos_clientes)

    if resp == 3:
        fb.totalizar_bus (matriz_asientos)

    if resp ==4: 
        fb.buscar_pasajero (matriz_datos_clientes)
    if resp == 5:
        break
    if resp ==6:
        print ("adios")                                  


                
            



                        
    
