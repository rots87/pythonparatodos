#!/usr/bin/env python

#Enteros

#Tipo dato entero ó int (desde -2^31 hasta 2^31)
entero = 23
print("El numero es:", entero)
print("Y su tipo es: ",  type(entero))

#Tipo dato Largo ó long ya no existe en la version 3.x de python

#Para convertir decimales a octales se añade un cero y una letra o minuscula (0o) al numero que vamos a poner
octal = 0o23 #Esto es un numero Octal
print("El numero es:", octal)
print("Y su tipo es: ",  type(octal))

#Para convertir decimales a Hexadecimales se añade un cero y una letra x minuscula (0x) al numero que vamos a poner
hexa = 0x23 #Esto es un numero Hexadecimal
print("El numero es:", hexa)
print("Y su tipo es: ",  type(hexa))

#Reales

#tipo de dato flotante o float
real = 0.2036
print("El numero es:", real)
print("Y su tipo es: ",  type(real))

#Tambien con notacion cientifica
real = 0.2036e-5
print("El numero es:", real)
print("Y su tipo es: ",  type(real))

#Complejos

complejo = 8 + 1j
print("El numero es:", complejo)
print("Y su tipo es: ",  type(complejo))
