"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista y la muestre por pantalla."""

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(subjects)

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de
 las asignaturas de la lista."""

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in range (len(subjects)):
    print (str("Yo estudio ") + str(subjects[i]) + str("."))

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla
 con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
  cada una de las correspondientes notas introducidas por el usuario."""

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista
 y los muestre por pantalla ordenados de menor a mayor."""

nwin = []

for i in range(6):
    nwin.append(int(input("¿Cuales son los numeros ganadores de la loteria: ")))
nwin.sort()
print("Los números ganadores son " + str(awarded))

"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso
 separados por comas."""

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number.sort(reverse=True)
print (number, end=",")

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y 
Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas 
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))

"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones
 múltiplos de 3, y muestre por pantalla la lista resultante."""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet), 1, -1):
       if i % 3 == 0:
           alphabet.pop(i-1)
print (alphabet)

"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

word = input("Inserta una palabra")
vocals = ['a', 'e', 'i', 'o', 'u']
count = [0, 0, 0, 0, 0]

for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")

"""Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por
 pantalla el menor y el mayor de los precios."""

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El mínimo es " + str(min))
print("El máximo es " + str(max))

"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto
 escalar."""

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))


"""Escribir un programa que almacene las matrices 𝐴=(142536)𝑦𝐵=⎛⎝⎜⎜⎜⎜⎜−101011⎞⎠⎟⎟⎟⎟⎟
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista."""

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])

"""Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y
 muestre por pantalla su media y desviación típica."""

sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)