"""
El usuario ingresa un numero y se muestra toda la secuencia fibonacci hasta ese numero.

Guarde los numeros en una lista.



Fibonacci.

1 1 2 3 5 8 13 21 34 ... i_n = i_n-1 + i_n-2

1) un elemento es la suma de los dos anteriores

2) los primeros dos elementos son 1
"""

numero = int(input("ingrese un numero:"))
numero1 = 1
numero2 = 0
numero3 = 0

lista = [0]
print("Fibonacci comenzando...")

for i in range (numero):
    numero3 = numero2 + numero1
    numero1 = numero2
    numero2 = numero3
    if numero3 > numero:
        break
    lista.append(numero3)

print(lista)
