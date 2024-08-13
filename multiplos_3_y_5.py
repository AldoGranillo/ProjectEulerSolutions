"""
Si enumeramos todos los números naturales a continuación 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9.
La suma de estos múltiplos es 23. Encuentra la suma de todos los múltiplos de 3 o 5 abajo 1000.
"""
almacen = 0
for i in range(1, 1000):
  if (i%3 == 0 or i%5 ==0):
    almacen +=i
print(almacen)