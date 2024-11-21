quesos = ["Cheddar", "Edam", "Gouda"]

print(quesos[2][3])

matriz = [
    [[1, 0, 0], [0, 2, 0], [0, 0, 3]],
    [[0, 4, 0], [0, 5, 1], [6, 0, 0]],
    [[0, 0, 7], [8, 0, 0], [0, 9, 0]],
]
print(matriz)
print(matriz[2])
print(matriz[2][0])
print(matriz[2][0][2])

matriz[2][0][2] = "patata"
print(matriz)

matriz[0] = "patata"
print(matriz)
