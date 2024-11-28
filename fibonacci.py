antepenultimo = 0
penultimo = 1
ultimo = 0
contador = 3

maximo = 3000000
limite = 513

print("1 -", antepenultimo)
print("2 -", penultimo)
# while ultimo < maximo:  # CONDICIÓN = ultimo < maximo
while contador <= limite:
    ultimo = penultimo + antepenultimo
    print(contador, "-", ultimo)
    antepenultimo = penultimo
    penultimo = ultimo
    contador += 1


