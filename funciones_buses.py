def ingresar_pasajero (matriz1,matriz2):
    nomb_pasajero="xx"
    while (len(nomb_pasajero))<3 or (len(nomb_pasajero))>10:
        try:
            nomb_pasajero = input("Ingrese el nombre del pasajero: ").upper()
            if (len(nomb_pasajero))<3 or (len(nomb_pasajero))>10:
                print("Nombre no valido, ingrese otro")
        except ValueError:
                print("Caracter no valido, ingrese el nombre correctamente:")

    rut_pasajero = "xx"
    while (len(rut_pasajero))<8 or (len(rut_pasajero))>9:
        try:               
            rut_pasajero = input("Ingrese el rut del pasajero: ")
            if (len(rut_pasajero))<8 or (len(rut_pasajero))>9:
                print ("Rut incorrecto, ingreselo nuevamente: ")
        except ValueError:
            print("Caracter erroneo, ingrese el rut nuevamente") 

    edad_pasajero = 1
    while edad_pasajero<18:
        try:
            edad_pasajero = int(input("Ingrese la edad del pasajero: "))
            if edad_pasajero<18:
                    print("Edad no valida, por favor, ingrese el dato nuevamente")
        except ValueError:
            print ("Carcarter invalido, por favor, ingrese la edad nuevamente")
            edad = 1
                        

    status =1
    while status == 1:
        try:
            asiento_pasajero = int(input("Ingrese el asiento que desea: "))
            if asiento_pasajero not in matriz1:
                    print("Asiento ocupado, por favor elija otro")
            for i in range (10):
                for j in range (4):

                    if matriz1[i,j] == asiento_pasajero:
                            matriz1[i,j] = "X"

                            dicc_datos_pasajero = {"nombre":nomb_pasajero,"rut":rut_pasajero,"edad":edad_pasajero,"sit":asiento_pasajero}
                            matriz2[i,j] = dicc_datos_pasajero

                            datos = f"Nombre: {nomb_pasajero}/ RUT:{rut_pasajero}/ Edad:{edad_pasajero}/ Asiento:{asiento_pasajero}\n"

                            with open ('datos.csv','a',newline='') as file:
                                file.write (datos)

                            with open ('log.txt','a') as archivo:
                                archivo.write (datos)

                            status = 2
        except ValueError:
            print ("Caracrter invalido, por favor, ingrese su eleccion nuevamente")
            status = 1   

def mostra_listado (matriz):
     for i in range (10):
            for j in range (4):  
                if matriz[i,j]!= "sin datos":  
                    print("")
                    print (f"Nombre: {matriz[i,j]["nombre"]}\tRUT:{matriz[i,j]["rut"]}\tEdad:{matriz[i,j]["edad"]}\tAsiento: {matriz[i,j]["sit"]}")
                    print("--------------------------------------------------------------------------------------------------")
                    print("")

def totalizar_bus (matriz):
    cont_diario = 0
    for i in range (10):
        for j in range (4):
            if matriz[i,j] == "X":
                cont_diario += 1
    print ("")            
    print("-------------------------------------")            
    print (f"Cantidad de pasajero: {cont_diario}")
    print (f"Total recaudado: {cont_diario*15000}")
    print("-------------------------------------")
    print ("") 

def buscar_pasajero (matriz):
    status = 1
    buscar_pasajero  = input("Ingrese el rut del pasajero que desea buscar:")
    for i in range (10):
        for j in range (4):
            if matriz [i,j] != "sin datos":
                if matriz [i,j]["rut"] == buscar_pasajero:
                    print ("Pasajero encontrado:")
                    print (f"Nombre: {matriz[i,j]["nombre"]}\tRUT: {matriz[i,j]["rut"]}\tEdad: {matriz[i,j]["edad"]}\tAsiento: {matriz[i,j]["sit"]}")   
                    status = 2             
    if status == 1:
        print ("Pasajero no encontrado")