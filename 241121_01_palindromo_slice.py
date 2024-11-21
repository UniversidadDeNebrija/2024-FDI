palabra_a_comprobar = "12344321"
print(palabra_a_comprobar)

if (palabra_a_comprobar == palabra_a_comprobar[::-1]):
    print("PALINDROMO")
else:
    print("Esta no")
