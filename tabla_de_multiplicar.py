## Obtener dtos de una lista de multiplicar del 6

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, numero in enumerate(numeros):
    total = numero * 6
    print(numero, "X 6 =", total)

## Recorrer solo los apellidos

datos = [["Maria", "Jose", "Laura", "Pedro"],
        ["Perez", "Lopez", "Garcia", "Cancino"]]

for i in datos[1]:
    print(i)