#Alumno: Barcelo Emmanuel
#Comision: 111
#UNICAMENTE VALIDA, EL MODULO GET SE ENCARGA DE PEDIR EL NUMERO O EL STRING
def validate_number(numero: int, maximo: int, minimo: int, mensaje_error: str, reintentos: int) -> bool:
    """
    Valida el dato.
    Parametros:
    Numero: El numero a validar. 
    Maximo: El maximo permitido.
    Minimo: El minimo permitido.
    mensaje_error: el mensaje mostrado en caso de que el dato sea incorrecto.
    Reintentos: El limite de veces que el usuario puede ingresar un dato.
    return
    Validacion: Devuelve el numero validado o None en caso de que sea incorrecto.
    """
    contador = 0
    validacion = numero
    while numero > maximo or numero < minimo:
        contador += 1
        if contador < reintentos:
            numero = int(input(mensaje_error))
            validacion = numero
        else: 
            validacion = None
            break
    return validacion

def validate_length(cadena: str, maximo: int, minimo: int, mensaje_error: str, reintentos: int) -> bool:
    """
    Valida el dato.
    Parametros:
    Numero: El numero a validar. 
    Maximo: El maximo permitido.
    Minimo: El minimo permitido.
    mensaje_error: el mensaje mostrado en caso de que el dato sea incorrecto.
    Reintentos: El limite de veces que el usuario puede ingresar un dato.
    return
    Validacion: Devuelve el numero validado o None en caso de que sea incorrecto.
    """
    contador = 0
    validacion = cadena
    while len(cadena) > maximo or len(cadena) < minimo:
        contador += 1
        if contador < reintentos:
            cadena = input(mensaje_error)
            validacion = cadena
        else: 
            validacion = None
            break
    return validacion
    










