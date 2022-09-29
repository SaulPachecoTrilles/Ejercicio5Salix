#from sys import platform, version jeje :)
#from sys import platform, version hola
from math import sin, cos, pi, sqrt


print('28 ¿Qué resulta de evaluar estas expresiones?')
print( '>>> str(2.1) + str(1.2)' )
print( str(2.1) + str(1.2) )
print( '>>> int( str(2) + str(3) )' )
print( int( str(2) + str(3) ) )
print( '>>> str( int(12.3) ) + "0"' )
print( str( int(12.3) ) + '0' )
print( '>>>int("2" +"3")' )
print( int('2' +'3') )
print( '>>>str(2+3)' )
print( str(2+3) )
print( '>>> str( int(2.1) + float(3) )' )
print( str( int(2.1) + float(3) ) )
print()

print('29 ¿Qué resultados se muestran al evaluar estas expresiones?')
print( '>>> "abalorio" < "abecedario"' )
print( 'abalorio' < 'abecedario' )
print( '>>> "abecedario" < "abecedario"' )
print( 'abecedario' < 'abecedario' )
print( '>>> "abecedario" <= "abecedario"' )
print( 'abecedario' <= 'abecedario' )
print( '>>> "Abecedario" < "abecedario"' )
print( 'Abecedario' < 'abecedario' )
print( '>>> "Abecedario" ==  "abecedario"' )
print( 'Abecedario' ==  'abecedario' )
print( '>>> 124 < 13')
print( 124 < 13 )
print( '>>> "124" < "13"')
print( '124' < '13')
print( '>>> " a" < "a"')
print( ' a' < 'a' )
print()

#print( sin(0) + ', ' + sin(1) + ', ' + cos(0) + ', ' + cos(1) ) //Libreria Math
#print( (1 +3j) / (2+1j) ) j = raiz de -1
#print( Decimal('0.1') ) // Dineros etc
#print( Fraction(2,4) ) // Fraction(1,2)
print('31 ¿Cuál será el resultado de evaluar estas expresiones?')
print( '>>> "{0}".format(1)' )
print( '{0}'.format(1) )
print( '>>> "{0} {1}".format(1, 2)' )
print( '{0} {1}'.format(1, 2) )
print( '>>> "{0}{1}".format(1, 2)' )
print( '{0}{1}'.format(1, 2) )
print( '>>> "{0}, {1}".format(1, 2)' )
print( '{0}, {1}'.format(1, 2) )
print( '>>> "{1}, {0}".format(1, 2)' )
print( '{1}, {0}'.format(1, 2) )
print( '>>> "{1}, {1}".format(1, 2)' )
print( '{1}, {1}'.format(1, 2) )
print( '>>> "{1}, 1".format(1, 2)' )
print( '{1}, 1'.format(1, 2) )
print()


#radio = float(input('Introduzca el valor del radio: '))
#perimetro = 2 * pi * radio
#volumen = 4/3 * pi * radio ** 3
#print( volumen )
#print( '%s' %(nombre))
print( '38 Diseña un programa que pida el valor de los tres lados de un triángulo y calcule el valor de su área y perímetro. Recuerda que el área A de un triángulo puede calcularse a partir de sus tres lados, a, b y b, así: A = √s(s - a)(s - b)(s - c), donde s = (a + b + c)/2. (Prueba que tu programa funciona correctamente con este ejemplo: si los lados miden 3, 5 y 7, el perímetro será 15.0 y el área 6.49519052838).' )
#Entrada de datos
a = float( input('Introduzca el valor del 1º lado: ') )
b = float( input('Introduzca el valor del 2º lado: ') )
c = float( input('Introduzca el valor del 3º lado: ')  )

#Calculos
perimetro = a + b + c
s = (a + b + c)/2
area = sqrt( s * (s-a) * (s-b) * (s-c) )

#Visualización de los resultados
print( 'El perimetro del triangulo es: {0:.1f} \nEl area del triangulo es: {1:.1f}'.format(perimetro, area) )
print()


print('41 Haz un programa que pida el nombre de una persona y lo muestre en pantalla repetido 1000 veces, pero dejando un espacio de separación entre aparición y aparición del nombre. (Utiliza los operadores de concatenación y repetición).')
nombre = input('Introduzca el nombre de la persona: ')
print( (nombre + ' ') * 1000 )
print()


