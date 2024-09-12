##Tarea

#Usando if, elif, y else, hacer un juego para adivinar un numero de 1 a 5:

# -> Se genera un numero aleatorio de 1 a 5.
# -> Se le pide al usuario ingresa un numero entero.

## Si el numero es igual al numero generado aleatoriamente imprimir: "Adivinaste el numero!"
## Si el numero es mayor que el numero generado aleatoriamente imprimir: "Muy alto"
## Si el numero es menor que el numero generado aleatoriamente imprimir: "Muy bajo"

import random

num_input = int(input("Ingresa un numero del 1 al 5: "))

if num_input not in [1, 2, 3, 4, 5]:
    raise Exception ("Opción inválida!")


random_num = random.choice([1, 2, 3, 4, 5])
print(f"Elección del computador (Computer's choice): {random_num}")
if random_num == num_input:
    print("Adivinaste el numero!")
elif num_input > random_num:
    print("Muy alto!")
elif num_input < random_num:
    print("Muy bajo!")