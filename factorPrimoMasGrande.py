"""
Los factores primos de 13195 son 5, 7, 13 y 29
¿Cuál es el factor primo más grande del número?
600851475143
"""

almacen = []
numero = 600851475144
for i in range(1, numero):
    if (600851475143 % i) == 0:
        almacen.append(i)
print(max(almacen))
