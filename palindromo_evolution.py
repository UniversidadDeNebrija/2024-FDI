def es_palindromo(palabra):
    print(f"[{palabra}]")
    print(f"[{palabra[::-1]}]")
    if palabra == palabra[::-1]:
        print("\033[92mPALINDROMO\033[0m")
    else:
        print("\033[31mNO\033[0m")

def sustituye_largo(palabra):
    sustituciones = [
        ["á", "a"], ["é", "e"], ["í", "i"], ["ó", "o"], ["ú", "u"],
        ["à", "a"], ["è", "e"], ["ì", "i"], ["ò", "o"], ["ù", "u"],
        ["ä", "a"], ["ë", "e"], ["ï", "i"], ["ö", "o"], ["ü", "u"],
        ["â", "a"], ["ê", "e"], ["î", "i"], ["ô", "o"], ["û", "u"]
    ]
    for sustitucion in sustituciones:
        palabra = palabra.replace(sustitucion[0], sustitucion[1])

    return palabra


def sustituye_corto(palabra):
    sustituciones = [
        "áéíóúàèìòùäëïöüâêîôû",
        "aeiouaeiouaeiuuaeiou"
    ]
    index = 0
    while index <= len(sustituciones[0]):
        letra_rara = sustituciones[0][index]
        letra_limpia = sustituciones[1][index]
        palabra = palabra.replace(letra_rara, letra_limpia)

    return palabra


def limpar(palabra_original):
    """
        palabra = palabra_original
        es_palindromo(palabra_original)
        palabra = palabra_original.strip()
        es_palindromo(palabra)
        palabra = palabra_original.lower()
        es_palindromo(palabra)
    """
    palabra = palabra_original.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace(",", "")
    palabra = palabra.replace(".", "")
    palabra = palabra.replace("!", "")
    palabra = palabra.replace("?", "")

    palabra = sustituye_corto(palabra)

    return palabra


def procesar(palabra_original):
    print(palabra_original)
    print("=========")
    es_palindromo(limpar(palabra_original))
    print()
    print()


lista_de_candidatos = [
    "Tu madre en vinagre",
    "Anita, la gorda lagartona, no traga la droga latina.",
    "Dábale arroz a la zorra el abad.",
    "Sé verlas al revés.",
    "La ruta nos aportó otro paso natural.",
    "Las Nemocón no comen sal.",
    "Anás usó tu auto, Susana.",
    "Esta no lo es",
    "Adán no cede con Eva, Yavé no cede con nada.",
    "Así Mario oirá misa.",
]

for frase in lista_de_candidatos:
    procesar(frase)
