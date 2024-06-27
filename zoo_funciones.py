def calcular_precio_entrada():
    precios = {
        'niños_gratis': 0,
        'niños_pago': 14,
        'adultos': 23,
        'jubilados': 18
    }

    conteo = {
        'niños_gratis': 0,
        'niños_pago': 0,
        'adultos': 0,
        'jubilados': 0
    }

    while True:
        edad_input = input("Introduce la edad del visitante (deja vacío para terminar): ")
        
        if edad_input == "":
            break
        
        if not edad_input.isdigit():
            print("Entrada no válida. Por favor, introduce un número entero positivo.")
            continue

        edad = int(edad_input)

        if edad < 0:
            print("Edad no válida. Por favor, introduce una edad positiva.")
            continue
        
        if edad <= 2:
            conteo['niños_gratis'] += 1
        elif edad <= 12:
            conteo['niños_pago'] += 1
        elif edad <= 64:
            conteo['adultos'] += 1
        else:
            conteo['jubilados'] += 1

    precio_total = (conteo['niños_gratis'] * precios['niños_gratis'] +
                    conteo['niños_pago'] * precios['niños_pago'] +
                    conteo['adultos'] * precios['adultos'] +
                    conteo['jubilados'] * precios['jubilados'])

    print(f"\nPrecio total del grupo: {precio_total} euros")
    print("Detalle por edades:")
    if conteo['niños_gratis'] > 0:
        print(f"Niños (0-2 años): {conteo['niños_gratis']} x {precios['niños_gratis']} euros = {conteo['niños_gratis'] * precios['niños_gratis']} euros")
    if conteo['niños_pago'] > 0:
        print(f"Niños (3-12 años): {conteo['niños_pago']} x {precios['niños_pago']} euros = {conteo['niños_pago'] * precios['niños_pago']} euros")
    if conteo['adultos'] > 0:
        print(f"Adultos (13-64 años): {conteo['adultos']} x {precios['adultos']} euros = {conteo['adultos'] * precios['adultos']} euros")
    if conteo['jubilados'] > 0:
        print(f"Jubilados (65+ años): {conteo['jubilados']} x {precios['jubilados']} euros = {conteo['jubilados'] * precios['jubilados']} euros")

if __name__ == "__main__":
    calcular_precio_entrada()
