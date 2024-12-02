from random import randint

class Coche:

    ruedas = 4                  # Atributo de clase (se comprate entre todos los coches
    cantidad = 0

    def __init__(self, color):  # Constructor del objeto
        Coche.cantidad += 1

        self.velocidad = 0      # Atributo de instancia # m/s
        self.color = color      # Atributo de instancia

    def acelerar(self, incremento):
        self.velocidad += incremento
    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
            print(f"el coche {self.color} se ha detenido")
    def destruir(self):
        Coche.cantidad -= 1
        print(f"El coche {self.color} estalla en mil pedacitos ")

class Carrera:
    def __init__(self):
        coche = Coche("negro")
        coches = [
            Coche("rojo"),
            Coche("verde"),
            Coche("azul"),
            Coche("blanco")
        ]
        coches.append(Coche("naranja"))
        coches.append(coche)

        for coche in coches:
            coche.acelerar(randint(10, 30))

        for coche in coches:
            if(coche.velocidad >= 20):
                coche.destruir()
            else:
                coche.frenar(30)


        print(f"En total quedan {Coche.cantidad} coches")

Carrera()