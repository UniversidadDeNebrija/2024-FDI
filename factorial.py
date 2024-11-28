def input_entero_positivo():
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Por favor, introduce un numero: "))
        except:
            print("ese numero no parece un entero")
        if numero < 0:
            print("El numero debe ser un entero POSITIVO")
    return numero


num_original = input_entero_positivo()
factorial = num_original
num = num_original


if num == 1:
    pass
elif num == 0:
    factorial = 1
else:
    while num > 1:
        num -= 1
        factorial *= num

print(num_original, "! = ", factorial)





