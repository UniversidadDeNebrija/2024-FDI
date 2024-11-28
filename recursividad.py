def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


for n in range(0, 11):
    print(n, " - ", factorial(n))


print(range(0, 11))
