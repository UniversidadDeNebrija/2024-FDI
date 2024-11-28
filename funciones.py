from random import randint


def devuelve_un_sobrino():
    num = randint(0, 2)

    if num == 0:
        return "Juanito"
    if num == 1:
        return "Jorgito"

    return "Jaimito"


dia = 0
while dia <= 7:
    dia += 1
    msg = "Dia " + str(dia) + " Donald vino con " + devuelve_un_sobrino()
    print(msg)
print("Menuda semanita")
