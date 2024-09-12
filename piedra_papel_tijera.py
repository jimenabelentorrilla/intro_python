## Juego de Piedra, Papel o Tijera
##Importa el archivo donde estan las funciones guardadas en random
import random

## El input siempre recibe un string por lo que no se necesita castearlo ( str() )
player_choice_input = input("Piedra (Rock), Papel (Paper), Tijera (Scissors) -> (r/p/s): " )

##Para no tener errores con las mayusculas, pasamos todos los valores a minuscula
player_choice = player_choice_input.lower()

## Un  not se utiliza para verificar que ese elemento no este en la lista predefinida
if player_choice not in ["r", "p", "s"]:
    ##Haremos una exepcion que diga opcion invalida
    raise Exception("Opcion Invalida!")

## De la libreria random, usa el metodo choice que recibe una lista de parametros
computer_choice = random.choice(["r", "p", "s"])
print(f"Elección del computador (Computer's choice): {computer_choice}")

## El doble igual (==) es para comparar por valor
## El is es para comparar objetos por referencia
if player_choice == computer_choice:
    print("Empate (Tie)")
elif player_choice == "r" and computer_choice == "s":
    print("Humano gana! (Player wins!)")
elif player_choice == "s" and computer_choice == "p":
    print("Humano wins! Player wins!")
elif player_choice == "p" and computer_choice == "r":
    print("Humano wins! Player wins!")
else:
    print("Computador gana! (Computer wins!)")