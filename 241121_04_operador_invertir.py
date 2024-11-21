def invertir(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida

    return palabra_invertida


def es_palindromo(palabra_a_comprobar):
    if palabra_a_comprobar == invertir(palabra_a_comprobar):
        return True

    return False

palabra_a_comprobar = "1234"
print(palabra_a_comprobar)
if (es_palindromo(palabra_a_comprobar)):
    print("PALINDROMO")
else:
    print("Esta no")
