# Comprobamos letra a letra. Optimo pero muy lioso
def es_palindromo(palabra_a_comprobar):
    longitud = len(palabra_a_comprobar)
    ultimo_indice_a_comprobar = int(longitud/2)

    for i in range(ultimo_indice_a_comprobar):
        indice_actual = i                                   # 0, 1, 2, 3, 4
        indice_espejo = longitud - indice_actual - 1

        letra_actual = palabra_a_comprobar[indice_actual]
        letra_espejo = palabra_a_comprobar[indice_espejo]

        print(f"{indice_actual} -- {indice_espejo}")
        print(f"{letra_actual} -- {letra_espejo}")

        if letra_actual != letra_espejo:
            return False

    return True



def invertir(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida

    return palabra_invertida


# optimo (argumento por defecto no)
def comprobar(palabra_a_comprobar, optimo = False):
    if optimo:
        return es_palindromo(palabra_a_comprobar)
    else:
        return palabra_a_comprobar == invertir(palabra_a_comprobar)

palabra_a_comprobar = "dabale arroz a la zorra el abad"
print(palabra_a_comprobar)
if (comprobar(palabra_a_comprobar, True)):
    print("PALINDROMO")
else:
    print("Esta no")
