def describir_char(char):
    print(char, " - ", ord(char), " - ", hex(ord(char)))


cadena = "Supercalifragilisticoespialidoso"
cadena = "oso"
longitud_de_la_cadena = len(cadena)

for letra in cadena:
    describir_char(letra)
for i in range(0, longitud_de_la_cadena):
    describir_char(cadena[i])



codigo = input("mete el Código: ")
print(codigo)