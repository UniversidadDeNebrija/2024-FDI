def es_palindromo(palabra_a_comprobar):
    mitad_entera_de_la_cadena = int(len(palabra_a_comprobar) / 2)
    indice_maximo_a_comprobar = mitad_entera_de_la_cadena
    indice = 0
    while indice < indice_maximo_a_comprobar:
        indice_espejo = len(palabra_a_comprobar) - (indice + 1)
        letra_a_comprobar = palabra_a_comprobar[indice]
        letra_espejo = palabra_a_comprobar[indice_espejo]
        if letra_a_comprobar != letra_espejo:
            return False
        indice += 1

    return True


palabra_a_comprobar = "abcdefghgfedcba"
print(palabra_a_comprobar)
if (es_palindromo(palabra_a_comprobar)):
    print("PALINDROMO")
else:
    print("Esta no")
