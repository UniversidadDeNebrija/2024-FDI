def comprueba_palindromo(palabra_original):
    limpia = palabra_original.lower()
    limpia = limpia.replace(" ", "")
    limpia = limpia.replace("á", "a")
    limpia = limpia.replace("\n", "")
    limpia = limpia.replace(".", "")
    limpia = limpia.replace(",", "")
    print(palabra_original)
    print(f"[{limpia}]")
    print(f"[{limpia[::-1]}]")

    print(("" if limpia == limpia[::-1] else "no ") + "PALINDROMO")


with open("texto_plano.txt") as manejador_fichero:
    for linea in manejador_fichero:
        comprueba_palindromo(linea)
        print("------------------------")
        print()
