## Crea una expresion que determine si un numero es positivo,
# negativo o igual a cero
numero = input("Digite un numero: ")

if int(numero) > 0: 
    print("El numero " + str(numero) + " es positivo")
elif int(numero) < 0:
    print("El numero " + str(numero) + " es negativo")
elif int(numero) == 0:
    print("El numero " + str(numero) + " es igual a 0")       