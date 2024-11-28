input_del_usuario = input("Por favor introduzca una temperatura en Cº: ")

try:
    celsius = float(input_del_usuario)
    fah = (celsius * 9 / 5) + 32
    relacion = fah / celsius
    print(fah, "Fº")
    print("Relación ", relacion)
except ValueError:
    print("No ha introducido una temperatura valida. por favor introduce solo numeros separados por un punto ej -21.9")
except ZeroDivisionError:
    print("Al ser 0, la relación es infinita")
except:
    print("A ocurrido algun otro tipo de error no manejado")

