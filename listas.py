import math

quesos = ["Cheddar", "Edam", "Gouda", "Cabrales", "Mozarella"]

quesos.pop(0,1)
print(quesos)

exit()


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

matriz[0] = math.pi
print(matriz)

# FALLA: pi no tinene indices, es un numero matriz[0][0][2]
