class Coche:

    modelo = None
    ruedas = None
    potencia = None
    color = None

    def __init__(self, modelo, ruedas, potencia, color):
        self.modelo = modelo
        self.ruedas = ruedas
        self.potencia = potencia
        self.color = color

    def acelerar(self):
        aceleracion = 1 / (self.potencia / 100)
        print(f"{self.modelo} acelera en { aceleracion } segundos")

    def frenar(self):
        pass

coche1 = Coche("488 Pista", 4, 600, "rojo")
coche2 = Coche("2CV", 4, 2, "blanco")


# Tipos
print(type(3.14))
print(type("patata"))
print(type([]))
print(type({}))
print(type(coche1))