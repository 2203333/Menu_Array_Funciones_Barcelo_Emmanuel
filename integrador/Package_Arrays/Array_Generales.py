from .Especificas import *

#opcion e:
def listar_numeros (lista_numeros: list):
    """
    Lista todos los numeros de una lista.
    Parametros:
    lista_numeros: la lista donde se encuentran los numeros
    """
    lista = lista_numeros 
    for i in range (len(lista)):
        print(f"{lista_numeros[i]}")

def listar_pares (lista_numeros: list):
    """
    Lista todos los numeros de una lista.
    Parametros:
    lista_numeros: la lista donde se encuentran los numeros
    return: 
    lista_pares: la lista de los numeros pares
    """
    lista_pares =  determinar_paridad(lista_numeros, "par")

    for i in range(len(lista_pares)):
        print(f"{lista_pares[i]}")
    
    return lista_pares
    
