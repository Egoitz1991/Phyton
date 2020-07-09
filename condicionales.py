"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""

edad = int(input("¿Que edad tienes?"))

while edad <= 0:
    edad = int(input("Inserta tu edad verdadera"))
if edad < 18:
    print ("Es menor de edad")
else:
    print ("Es mayor de edad")

"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la
 contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
 sin tener en cuenta mayúsculas y minúsculas."""

pass_1 = input("Inserta una contraseña")

pass_2 = input("Inserta la contraseña de nuevo")

if pass_1 == pass_2:
    print ("Es la misma contraseña")
else:
    print ("La contraseña es diferente")

"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el
programa debe mostrar un error."""

numero_1 = float(input("Inserta un numero"))
numero_2 = float(input("Inserta su divisor"))

while numero_2 == 0:
    print("El divisor no puede ser 0")
    numero_2 = float (input("Inserta otro divisor valido"))

"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""

numero_1 = int(input("Inserta un numero entero"))

if numero_1 / 2 == 0:
    print ("Es par")
else:
    print ("Es impar")

"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 €
mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
 usuario tiene que tributar o no."""

edad = int(input("Inserta tu edad"))

while edad <= 0:
    edad = int(input("Inserta una edad valida"))

tributo = float(input("Inserta tus ingresos"))

if tributo >= 1000:
    print ("Debes tributar")
else:
    print ("No debes tributar")

"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado
por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
 Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")

if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

    Renta	                Tipo impositivo
Menos de 10000€	                5%
Entre 10000€ y 20000€	        15%
Entre 200000€ y 35000€	        20%
Entre 350000€ y 60000€	        30%
Más de 60000€	                45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""

renta = int(input("Inserta tu renta anual"))

if renta < 10000:
    print ("El tipo impositivo es de 5%")
elif renta > 10000 and renta <= 20000:
    print ("El  tipo impositivo es del 15%")
elif renta > 20000 and renta <= 35000:
    print ("El tipo impositivo es del 20%")
elif renta > 35000 and renta <= 60000:
    print ("El tipo impositivo es del 30%")
elif renta > 60000:
    print ("El tipo impositivo es del 45%")

"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la
evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación
se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero
que recibirá el usuario."""

points = float (input("Inserta tu puntuacion"))

while points % 0.2 != 0:
    points = float (input("Inserta una puntuacion valida"))

euros = 2400 * points

print (str("Tu nivel de rendimiento ha sido ") + str(points) + str(" y el dinero que vas a percibir es de ") + str(euros)
       + str("."))


"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma 
automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente 
y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años 
debe pagar 5€ y si es mayor de 18 años, 10€."""

edad = int(input("¿Cuantos años tienes"))

while edad <= 0:
    edad = int(input("¿Cuantos años tienes de verdad?"))

if edad < 4:
    print ("Puedes entrar gratis")
elif edad >= 4 and edad <= 18:
    print ("Debes pagar 5€")
else:
    print ("Has de pagar 10€")

"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada
tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le
muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
vegetariana o no y todos los ingredientes que lleva."""

bool = input("¿Quieres una pizza vegetariana?")

veg = ['pimiento', 'tofu']
noveg = ['peperoni', 'jamon', 'salmon']

if bool == 'si' or bool == 'Si' or bool == 'SI':
    print (str("Puedes elegir entre los siguientes ingredientes:"))
    for ing in range(0, len(veg)):
        print (veg[ing])
else:
    print(str("Puedes elegir entre los siguientes ingredientes:"))
    for ing in range(0, len(noveg)):
        print (noveg[ing])