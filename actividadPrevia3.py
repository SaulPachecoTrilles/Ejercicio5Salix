print( '56 Indica qué líneas del último programa (y en qué orden) se ejecutarán para cada uno de los siguientes casos: ')
print( 'Programa para la resolución de la ecuación a x + b = 0 ')

#Entrada de datos
a = int( input('Introduzca el valor de a: ') )
b = int( input('Introduzca el valor de b: ') )

#Cálculos
if a != 0:
    x = -b / a
    print('Solución: ', x)

if a == 0 :
    if b != 0:
        print('La ecuación no tiene solución.')
    if b == 0:
        print('La ecuación tiene infinitas soluciones')

print( '59 Diseña un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.' )
#Entrada de datos
edad1 = int( input('Introduzca la edad de la 1º persona: ') )
edad2 = int( input('Introduzca la edad de la 2º persona: ') )

#Cálculos
res = ''
if edad1 > edad2:
    res = 'La primera persona es mas mayor.'

if edad2 > edad1:
    res = 'La segunda persona es mas mayor.'

if edad1 == edad2:
    res = 'Las dos personas tienen la misma edad.'

#Visualización
print(res)

print( '63 Diseña un programa que, dado un número entero, muestre por pantalla el mensaje «El número es par.» cuando el número sea par y el mensaje «El número es impar.» cuando sea impar.' )
#Entrada de datos
num = int( input('Introduzca el numero entero: ') )

#Cálculos
res = ''
if num % 2 == 0:
    res = 'El número es par.'
if num % 2 != 0:
    res = 'El número es impar.'

#Visualización
print(res)

print( '64 Diseña un programa que, dado un número entero, determine si este es el doble de un número impar.' )
#Entrada de datos
num = int( input('Introduzca el numero entero, para determinar si este es el doble de un numero impar o no: ') )

#Cálculos
res = ''
if num % 2 == 0 and (num/2) % 2 != 0:
    res = 'El número es el doble de un número impar.'

#Visualización
print(res)


print( '70 Diseña un programa Python que lea un carácter cualquiera desde el teclado, y muestre el mensaje «Es una MAYÚSCULA» cuando el carácter sea una letra mayúscula y el mensaje «Es una MINÚSCULA» cuando sea una minúscula. En cualquier otro caso, no mostrará mensaje alguno. (Considera únicamente letras del alfabeto inglés). Pista: aunque parezca una obviedad, recuerda que una letra es minúscula si está entre la "a" y la "z", y mayúscula si está entre la "A" y la "Z".' )

#Entrada de datos
cadena = input('Introduzca el carácter: ')

'''Esto esta mal acepta digitos y caracteres
if cadena == cadena.lower():
    res = 'Es una MINÚSCULA'
if cadena == cadena.upper():
    res = 'Es una MAYÚSCULA'
'''
#Cálculos 
res =''
if cadena >= 'a' and cadena <= 'z':
    res = 'Es una MINÚSCULA'

if cadena >= 'A' and cadena <= 'Z':
    res = 'Es una MAYÚSCULA'

#Visualización
print(res)


print( '71 Amplía la solución al ejercicio anterior para que cuando el carácter introducido no sea una letra muestre el mensaje «No es una letra».' )
#Entrada de datos
cadena = input('Introduzca el carácter: ')

#Cálculos
res =''

if cadena >= 'a' and cadena <= 'z':
    res = 'Es una MINÚSCULA'
elif cadena >= 'A' and cadena <= 'Z':
    res = 'Es una MAYÚSCULA'
else:
    res = 'No es una letra'

#Visualización
print(res)
