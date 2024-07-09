from zoo_funciones import pide_edad, procesa_entrada, tipos_entrada
from simple_screen import Screen_manager, Print, Input, locate

with Screen_manager:
    while True:
        edad = pide_edad()
        
        if edad == "":
            break

        procesa_entrada(edad)

    total = 0
    locate(0, 4)
    for tipo, valores in tipos_entrada.items():
        subtotal = valores['CONTADOR'] * valores['PRECIO']
        Print(f"{valores['CONTADOR']} de {tipo}: {subtotal:.2f} Euros")
        total = total
    
    locate(2,9,"Pulsa una tecla para terminar")
    Input()
