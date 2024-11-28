eng2sp = {
    "film": "película",
    "phone": "teléfono",
    "house": "casa"
}

mi_dicc = eng2sp.copy()

mi_dicc["phone"] = 33

print(eng2sp)

diccionario_frutas = {
    'Plátano': 1.35,
    'Manzana': ['a', 2, 3.33],
    'Pera': "si por favor",
    'Naranja': 0.7
}

print("-----------------------")
print(diccionario_frutas['Pera'])
print(diccionario_frutas['Manzana'][2])
print("====================")
lista = diccionario_frutas['Manzana']
print(lista[2])


exit()
for llave in diccionario_frutas:
    print(f"{llave}")
    print(f"{diccionario_frutas[llave]}")
