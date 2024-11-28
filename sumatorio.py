def introducir_entero():
    try:
        return int(input("Introduce un número: "))
    except ValueError:
        return introducir_entero()

num = None
suma_total = 0
while num != 0:
    num = int(input("Introduce un número: "))
    suma_total += num

print(f"la suma es igual a {suma_total}")




