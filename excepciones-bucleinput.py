def solicitar_entero():
    entero = None
    while entero is None:
        try:
            entero = int(input("introduce un entero: "))
        except ValueError:
            print("Eso no es un entero válido")

    return entero

print(solicitar_entero())