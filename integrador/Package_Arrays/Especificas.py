from .Array_Generales import *

#OPCION B
def mostrar_positivos_negativos(lista_numeros: list, criterio: str) -> int:
    """
    Determina si los numeros de una lista son negativos o positivos.
    parametros:
    lista_numeros: la lista donde se encuentran los numeros.
    criterio: segun el criterio, devolvera la cantidad de numeros positivos o negativos.
    return:
    resultado: la cantidad de numeros positivos o negativos encontrados.

    """
    positivos = 0
    negativos = 0
    
    for i in range (len(lista_numeros)):
        if lista_numeros[i] >= 0:
            positivos += 1
        else: 
            negativos += 1

    if criterio == "positivos":
        resultado = positivos
    else:
        resultado = negativos
    
    return resultado

def determinar_paridad(lista_numeros: list, criterio: str) -> list:
    """
    Determina si los numeros de una lista son pares o impares.
    parametros:
    lista_numeros: la lista donde se encuentran los numeros.
    criterio: segun el criterio, devolvera la lista de numeros pares o impares.
    return:
    lista: la lista de numeros pares o impares que retornara la funcion.

    """
    lista_par = []
    lista_impar = []

    for i in range(len(lista_numeros)):
        if lista_numeros[i] % 2 == 0:
            lista_par += [lista_numeros[i]]
        else:
            lista_impar += [lista_numeros[i]]
    
    if criterio == "par":
        lista = lista_par
    else:
        if criterio == "impar":
            lista = lista_impar

    return lista

#OPCION C:
def sumar_pares(lista_numeros: list) -> int:
    """
    suma los numeros pares de una lista.
    parametros:
    lista_numeros: la lista donde se encuentran los numeros.
    return:
    suma: la suma de los numeros.
    """
    lista_pares = determinar_paridad(lista_numeros, "par")
    suma = 0

    for i in range(len(lista_pares)):
        suma += lista_pares[i]

    return suma

#OPCION D:
def calcular_maximo_impar(lista_numeros: list) -> int:
    """
    Calcula el mayor de los numeros impares de una lista.
    parametros:
    lista_numeros: la lista donde se encuentran los numeros.
    return:
    maximo: El mayor numero encontrado"""
    bandera = False
    lista_impares = determinar_paridad(lista_numeros, "impar")
    
    for i in range (len(lista_impares)):
        if bandera == False or lista_impares[i] > maximo:
            maximo = lista_impares [i]
            bandera = True
    
    return maximo


#OPCION G:
def listar_posiciones_impares(lista_numeros: list) -> list:
    posiciones_impares = []
    for i in range (len(lista_numeros)):
        if i % 2 == 0:
            posiciones_impares += [lista_numeros[i]]

    return posiciones_impares




