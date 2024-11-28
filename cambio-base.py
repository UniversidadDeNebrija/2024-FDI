def decimal_a_binario(num):
    numero = 0
    # Completar el código aquí
    binario = bin(num)
    return binario

numero = int(input("Introduce un número: "))
print("El número en binario es:", decimal_a_binario(numero))
