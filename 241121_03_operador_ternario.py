palabra_a_comprobar = "12344321"
print(palabra_a_comprobar)

# condicion puede ser True o False
condicion = palabra_a_comprobar == palabra_a_comprobar[::-1]

if condicion:
    print("PALINDROMO")
else:
    print("Esta no")

print("SI" if condicion else "NO") # EQUIVALENTE AL IF ELSE

nota = 4.9
estado = "APROBADO" if nota > 5 else "SUSPENDIDO"

