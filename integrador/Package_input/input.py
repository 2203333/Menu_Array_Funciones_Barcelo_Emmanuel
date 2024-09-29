from Package_input.validate import validate_number, validate_length

def get_int(mensaje: str, maximo: int, minimo: int, mensaje_error: str, reintentos: int, mensaje_final: str) ->int:
    """
    Pide el dato y llama a la funcion validate para validarlo
    Parametros:
    Mensaje: El mensaje que se le muestra al usuario al pedir el numero.
    Maximo: El maximo permitido.
    Minimo: El minimo permitido.
    mensaje_error: el mensaje mostrado en caso de que el dato sea incorrecto.
    Reintentos: El limite de veces que el usuario puede ingresar un dato.
    Mensaje_final: Mensaje mostrado en caso de que el usuario se quede sin reintentos.
    return
    Resultado: numero ingresado o mensaje de error final
    """
    numero = int(input(mensaje))
    validacion = validate_number(numero, maximo, minimo, mensaje_error, reintentos)
    if validacion == None:
        resultado = mensaje_final
    else: 
        resultado = validacion
    return resultado

def get_float(mensaje: str, maximo: int, minimo: int, mensaje_error: str, reintentos: int, mensaje_final: str) ->float:
    """
    Pide el dato y llama a la funcion validate para validarlo
    Parametros:
    Mensaje: El mensaje que se le muestra al usuario al pedir el numero.
    Maximo: El maximo permitido.
    Minimo: El minimo permitido.
    mensaje_error: el mensaje mostrado en caso de que el dato sea incorrecto.
    Reintentos: El limite de veces que el usuario puede ingresar un dato.
    Mensaje_final: Mensaje mostrado en caso de que el usuario se quede sin reintentos.
    return
    Resultado: numero ingresado o mensaje de error final
    """
    numero = float(input(mensaje))
    validacion = validate_number(numero, maximo, minimo, mensaje_error, reintentos)
    if validacion == None:
        resultado = mensaje_final
    else: 
        resultado = validacion
    return resultado


def get_string(mensaje: str, maximo: int, minimo: int, mensaje_error: str, reintentos: int, mensaje_final: str) -> str:
    """
    Pide el dato y llama a la funcion validate para validarlo
    Parametros:
    Mensaje: El mensaje que se le muestra al usuario al pedir el numero.
    Maximo: El maximo permitido.
    Minimo: El minimo permitido.
    mensaje_error: el mensaje mostrado en caso de que el dato sea incorrecto.
    Reintentos: El limite de veces que el usuario puede ingresar un dato.
    Mensaje_final: Mensaje mostrado en caso de que el usuario se quede sin reintentos.
    return
    Resultado: numero ingresado o mensaje de error final
    """
    cadena = input("Ingrese una cadena: ")
    validacion = validate_length(cadena, maximo, minimo, mensaje_error, reintentos)
    if validacion == None:
        resultado = mensaje_final
    else: 
        resultado = validacion
    return resultado

