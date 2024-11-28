import math
from random import randint

dinero = randint(0, 10000)
PRECIO_FERRARI = 8000
PRECIO_BMW = 5000
PRECIO_PEUGEOT = 2000
PRECIO_DACIA = 1000

if dinero >= PRECIO_FERRARI:
    msg = "da para el Ferrari"
    print(msg)
elif dinero >= PRECIO_BMW:
    print("Tenemos BMW, vamooos!!!!")
elif dinero >= PRECIO_PEUGEOT:
    print("Un Peugeot, nostamal")
elif dinero >= PRECIO_DACIA:
    print("Un Dacia, al menos tenemos ruedas")
else:
    print("abra que pensar en un patinete")

print("Tenias " + str(dinero) + " EUROS")


