numero = int(input("introduce un número: "))

if numero <= 1:
    print("Por favor, introduce un nunmero ms grande (NO PRIMO POR DEFINICIÓN)")
    exit()

divisor = 2
raiz = numero ** 1/2

while divisor < raiz:
    if numero % divisor == 0:
        print("NO PRIMO (divisible por", divisor, ")" )
        exit()
    else:
        divisor += 1

print("SI ES PRIMO!!!!!")
