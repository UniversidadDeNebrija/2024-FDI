def decimal_a_binario(num):
    # código aqui
    binario = bin(num)
    return binario

numero = int(input("introduce un número: "))
print("El número en binario es:", decimal_a_binario(numero))
