input_del_usuario = input("Por favor introduzca una temperatura en Cº: ")

try:
    celsius = float(input_del_usuario)
except:
    print("No ha introducido una temperatura valida. por favor introduce solo numeros separados por un punto ej -21.9")
    exit()
fah = (celsius * 9/5) + 32

print(fah, "Fº")

try:
    relacion = fah / celsius
    print("Relación ", relacion)
except ZeroDivisionError:
    print("Al ser 0, la relación es infinita")


