##Ejercicio 3

##Menu restaurante

##Pedir el nombre del cliente
## Saludar al comensal
## Imprimir 3 opciones de menu que son 3 variables texto diferentes
## Luego pedir cual opcion del menu quiere que la escriba
## Luego pedir la direccion de entrega
## Tener una variable que guarde el tiempo de entrega predeterminado
## Luego imprimir "Hola NOMBRE, su pedido de PLATO, sera llevado en TIEMPO DE ENTREGA a DIRECCION"

nombre = input("Por favor ingrese su nombre: ")

print("Hola " + nombre + " " + "bienvenido/a a nuestro restó!")

## carta = ("spaguetti", "mate", "sarasa") MAL
# ##print("Nuestra carta de hoy tiene estas opciones: " + str(carta)) MAL


spaguetti_carbonara = "Opción 1: Spaguetti a la Carbonara"
ensalada = "Opción 2: Ensalada de arroz con atún"
empanadas = "Opción 3: Empanadas de carne cortada a cuchillo"
print("Nuestra carta de hoy tiene estas opciones: \n")
print(spaguetti_carbonara)
print(ensalada)
print(empanadas)

plato = input("¿Qué querés comer hoy? ")
direccion = input("¿Dónde estás ubicado? Pasanos tu dirección: ")

##Al ser una constante DEBE estar en mayúscula
TIEMPO_ENTREGA = 30

print("Hola " + nombre + " su pedido de " + plato + " será llevado en " + str(TIEMPO_ENTREGA) + " " + "minutos a " + str(direccion))