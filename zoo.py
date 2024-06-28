tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

def es_entero_menor_de_100_y_no_negativo(cadena: str) -> bool:
    result = False
    try:
        numero = int(cadena)
        if numero < 0 or numero > 99:
            result = False
        else:
            result = True
    except ValueError:
        result = False

    return result


def pide_edad():
    '''
    Pide el dato con el mensaje debido
    y devuelve o "" si se ha pulsado enter
    o un numero entero introducido por el usuario
    en otro caso vuelve a pedir

    '''
    while True:
        edad = input("Dime Edad: ")
        if edad == "":
            break
        elif not es_entero_menor_de_100_y_no_negativo(edad):
            print("introduce un numero entre 0 y 99")
            continue
        else:
            edad = int(edad)
            break
        
    return edad


def procesa_entrada(edad: int):
    if edad < 3:
        tipos_entrada["BEBE"]["CONTADOR"] = tipos_entrada["BEBE"]["CONTADOR"] + 1
    elif edad < 13:
        tipos_entrada["NIÑO"]["CONTADOR"] = tipos_entrada["NIÑO"]["CONTADOR"] + 1
    elif edad < 65:
        tipos_entrada["ADULTO"]["CONTADOR"] = tipos_entrada["ADULTO"]["CONTADOR"] + 1
    else:
        tipos_entrada["JUBILADO"]["CONTADOR"] = tipos_entrada["JUBILADO"]["CONTADOR"] + 1