# Definir un diccionario
tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

entrada_usuario = None

while True:
    entrada_usuario = input("Edad: ")
    if entrada_usuario == '':  # Si el usuario no ingresa nada y presiona enter, el programa se termina.
        break
    try:
        edad = int(entrada_usuario)  # Intentar convertir a un entero lo que ingreso el usuario 
        if edad < 3:
            tipos_entrada["BEBE"]["CONTADOR"] += 1
        elif edad < 13:
            tipos_entrada["NIÑO"]["CONTADOR"] += 1
        elif edad < 65:
            tipos_entrada["ADULTO"]["CONTADOR"] += 1
        else:
            tipos_entrada["JUBILADO"]["CONTADOR"] += 1
    except ValueError: 
        print("Ingresa un número válido")

total = 0
for tipo, valores in tipos_entrada.items():
    cantidad_entradas = valores['CONTADOR']
    subtotal = cantidad_entradas * valores['PRECIO']
    print(f"{cantidad_entradas} {'entrada' if cantidad_entradas == 1 else 'entradas'} de {tipo}: {subtotal:.2f} €")  # Muestra en pantalla el resultado al usuario 
    total += subtotal
print("----------")
print(f"TOTAL: {total:.2f} €")