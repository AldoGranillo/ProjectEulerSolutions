"""
Cada nuevo término en la secuencia de Fibonacci se genera sumando los dos términos anteriores.
Al comenzar con 1 y 2, los primeros 10 términos serán: 1,2,3,5,8,13,21,34,55,89,.....
Considerando los términos de la secuencia de Fibonacci cuyos valores
no superan los cuatro millones, encuentre la suma de los términos pares.
"""
actual =0
siguiente=1
suma=1
almacen=0
for i in range(33):
  suma= actual +siguiente
  #print(f"numero {i} = {suma}")
  actual = siguiente
  siguiente = suma
  if(suma%2==0):
    #print(suma)
    almacen+=suma
print(f"la suma de los pares son: {almacen}")