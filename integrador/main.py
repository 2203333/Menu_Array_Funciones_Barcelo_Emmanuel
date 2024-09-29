from os import system
from Package_Arrays.Array_Generales import *
from Package_Arrays.Especificas import *
from Package_input.input import get_int

numeros_ingresados = False
lista_numeros = [0] *10
while True:
    opcion = input("1. Ingresar numeros.\n2. Mostrar la cantidad de numeros positivos y negativos.\
          \n3. Mostrar la sumatoria de los números pares.\n4. Informar el mayor de los números impares.\
          \n5. Listar todos los números ingresados. \n6. Listar todos los números pares.\
          \n7. Listar los números de las posiciones impares. \n8. Salir. \nElija una opcion: ")
    
    match opcion:
        case "1":
            for i in range(10):
                lista_numeros[i] = get_int("Ingrese un numero: ", 1000, -1000,
                                           "Numero invalido. Recuerde que el rango aceptado es entre 1000 y -1000: ",
                                            5, "Ingreso de datos invalido.")
            numeros_ingresados = True
    
        case "2":
            if numeros_ingresados == True:
                positivos = mostrar_positivos_negativos(lista_numeros, "positivos")
                negativos = mostrar_positivos_negativos(lista_numeros, "negativos")
                print(f"La cantidad de numeros positivos es: {positivos} y la cantidad de numeros negativos es: {negativos}")
            else:
                print("No puede utilizar esta opcion. Asegurese de ingresar los datos en la opcion 1.")
        
        case "3":
            if numeros_ingresados == True:
                suma_pares = sumar_pares(lista_numeros)
                print(f"La suma de todos los numeros pares es: {suma_pares}")
            else:
                print("No puede utilizar esta opcion. Asegurese de ingresar los datos en la opcion 1.")

        
        case "4":
            if numeros_ingresados == True:
                maximo_impar = calcular_maximo_impar(lista_numeros)
                print(f"El numero impar mas grande es: {maximo_impar}")
            else:
                print("No puede utilizar esta opcion. Asegurese de ingresar los datos en la opcion 1.")


        
        case "5":
            if numeros_ingresados == True:
                print("Los numeros ingresados son:")
                listar_numeros(lista_numeros)
            else:
                print("No puede utilizar esta opcion. Asegurese de ingresar los datos en la opcion 1.")



        case "6":
            if numeros_ingresados == True:
                print("Los numeros pares ingresados son:")
                listar_pares(lista_numeros)
            else:
                print("No puede utilizar esta opcion. Asegurese de ingresar los datos en la opcion 1.")

            
        
        case "7":
            if numeros_ingresados == True:
                posiciones_impares = listar_posiciones_impares(lista_numeros)
                for i in range (len(posiciones_impares)):
                    print(f"{posiciones_impares[i]}")
            else:
                print("No puede utilizar esta opcion. Asegurese de ingresar los datos en la opcion 1.")

        
        case "8":
            print("Gracias por usar el programa.")
            break
    system ("pause")
    system ("cls")

    

    
