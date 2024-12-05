from random import randint


class Scoville():
    techo = 16000000

    def __init__(self, max, min=0):
        self.min = min
        self.max = max

    def __str__(self):
        return f"[{self.min} - {self.max}] shu"

    def suerte(self):
        return randint(self.min, self.max)


S = Scoville


class Pimiento:
    totalVariedades = 0
    cantidadTotal = 0


    def __init__(self, nombre="NO_NAME", scoville=None, tipo=None):
        self.variedad = nombre.lower()
        self.scoville = scoville
        self.tipo = tipo
        self.cantidad = randint(1,100)
        Pimiento.cantidadTotal += self.cantidad

        Pimiento.totalVariedades += 1

    def __str__(self):
        msg = "\n"
        msg += f"Nombre:   {self.variedad.capitalize()}\n"
        msg += f"Tipo:     {self.tipo.capitalize()}\n"
        msg += f"Kg:       {self.cantidad}\n"
        msg += f"Scoville: {self.scoville}"
        return msg

pimiento = {
    "piparra": Pimiento("piparra", S(500, 100), "dulce"),
    "cayena": Pimiento("cayena", S(80000, 50000), "picante"),
    "italiano": Pimiento("italiano", S(5000, 1000), "dulce"),
    "padrón": Pimiento("padrón", S(1000, 0), "dulce"),
    "ñora": Pimiento("ñora", S(1000, 500), "dulce"),
    "California": Pimiento("California", S(1000, 0), "dulce"),
    "morrón": Pimiento("morrón", S(1000, 0), "dulce"),
    "guindilla": Pimiento("guindilla", S(50000, 20000), "picante"),
    "jalapeño": Pimiento("jalapeño", S(8000, 3500), "picante"),
    "Cayena": Pimiento("Cayena", S(50000, 30000), "picante"),
    "topepo": Pimiento("topepo", S(500, 100), "dulce"),
    "tabasco": Pimiento("tabasco", S(50000, 25000), "picante"),
    "chipotle": Pimiento("chipotle", S(50000, 20000), "picante"),
}

# for llave in pimiento:
#     print(pimiento[llave])

print(f"Total de variedades: {Pimiento.totalVariedades}")
print(f"Total de Kg: {Pimiento.cantidadTotal}")

print(pimiento["ñora"])
picantePorKilo = pimiento["ñora"].scoville.suerte() / pimiento["ñora"].cantidad
print(f"Picante Por Kg: {picantePorKilo}")
print(f"Aportacion total: {picantePorKilo / Pimiento.cantidadTotal}")


invenatu = Pimiento("INVENTAU", S(min=50000, max=100000), tipo="Falso como una moneda de judas")


print(invenatu)
picantePorKilo = invenatu.scoville.suerte() / invenatu.cantidad
print(f"Picante Por Kg: {picantePorKilo}")
print(f"Aportacion total: {picantePorKilo / invenatu.cantidadTotal}")