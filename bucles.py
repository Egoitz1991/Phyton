"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

word = input("Inserta una palabra")

for contador in range(10):
    print(word)

"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
(desde 1 hasta su edad)."""

edad = int(input("Ingresa tu edad"))

while edad <= 0:
    edad = int(input("Ingresa tu edad verdadera"))

for contador in range(edad):
    print(contador + 1)

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números 
impares desde 1 hasta ese número separados por comas."""

numero = int(input("Inserta un numero entero positivo"))

while numero < 0:
    numero = int(input("Inserta un numero entero positivo correcto"))

for contador in range(1, n+1, 2):
    print(contador, end=", ")

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde 
ese número hasta cero separados por comas."""

numero = int(input("Inserta un numero entero positivo"))

while numero < 0:
    numero = int(input("Inserta un numero entero positivo correcto"))

for contador in range(numerom -1, -1):
    print(contador, end=", ")

"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre
 por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))

for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i + 1) + " años: " + str(round(amount, 2)))

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el 
de más abajo, de altura el número introducido."""

numero = int(input("Inserta un numero entero"))

for i in range(numero):
    for j in range(i + 1):
        print("*", end="")
    print("")

"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

cont = 1
mult = 10

while cont <= 10:
    print(cont * mult)
    cont = cont + 1

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como 
el de más abajo."""

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta."""

pass_1 = input("Inserta una contraseña")
pass_2 = input("Inserta la contraseña")

while pass_1 != pass_2:
    pass_2 = input("Inserta de nuevo la contraseña")

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra
 introducida empezando por la última."""

word = input("Inserta una palabra")

for i in range (len(word)-1, -1, -1):
    print(word[i])


"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de 
veces que aparece la letra en la frase."""

letter = input("Inserta una letra")
sent = input("Inserta una frase")
count = 0

for i in sent:
    if i == letter:
        count += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letter, count, sent))

"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” 
que terminará."""

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)