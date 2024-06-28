from zoo import pide_edad, procesa_entrada, tipos_entrada

while True:
    edad = pide_edad()
    
    if edad == "":
        break

    procesa_entrada(edad)

total = 0
for tipo, valores in tipos_entrada.items():
    subtotal = valores['CONTADOR'] * valores['PRECIO']
    print(f"{valores['CONTADOR']} de {tipo}: {subtotal:.2f} Euros")
    total = total