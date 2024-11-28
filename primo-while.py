def es_primo(num):
    # Los números menores o iguales a 1 no son primos
    if num <= 1:
        return False
    divisor = 2
    # Usamos un bucle while para verificar divisores hasta la raíz cuadrada del número
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

# Pedir al usuario que introduzca un número
numero = int(input("Introduce un número: "))

# Verificar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
