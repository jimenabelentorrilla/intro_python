## Obtener el index y valor de un arreglo en un ciclo
## Para obtener el index y valor vamos a usar la funcion enumerate
# Sintaxis: enumerate(iterable, start = 0)
# Parámetros:
# Iterable: cualquier objeto que admita iteración
# Inicio: el valor del indice desde el cual se iniciará el contador, por defecto es 0
# Retorno: Devuelve un iterador con pares de indices y elementos del iterable original
numeros = [1,2,3,4,5,6,7,8,9,10]
for index, numero in enumerate(numeros):
    print("Posición: ", index, "Numero: ", numero)

## Obtener dtos de una lista de multiplicar del 6

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, numero in enumerate(numeros):
    total = numero * 6
    print(numero, "X 6 =", total)
## Un arreglo bidimensional es una estructura de datos que contiene otros arrays como elementos.
## Recorrer solo los apellidos

datos = [["Maria", "Jose", "Laura", "Pedro"],
        ["Perez", "Lopez", "Garcia", "Cancino"]]

for i in datos[1]:
    print(i)