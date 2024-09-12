## Declaraciones y expresiones

## Declaraciones en Python
## Una declaración de asignación evalúa la lista de expresiones (puede ser una única) 
## expresión o una lista separada por comas, la ultima produce una tupla)
## Y asigna el único objeto resultante a cada una de las listas de objetivos, de izquierda a derecha.

a, b, c = 1, 2, 3

a = 1
b = 2
c = 3  

## Tipos de declaraciones

## Declaraciones de asignación
## Declaraciones de control de flujo (if, else, elif, while, for)

# FOR - sirve para recorrer elementos de un iterable, puede ser una lista, una tupla, un generador etc...
# Es una palabra reservada para un bucle
# I, J y K se utilizan para hacer uso de los ciclos
for i in a:
    print(i)
    ## A la variable i le va asignando cada uno de los elementos que esta dentro del iterable (en este caso una lista)

for i in range(0, 4, 1):
    ## En donde le pasamos por parametro el inicio (inclusivo), el final (exclusivo) y de cuanto en cuanto quiero mostrarlo
    print(i)
    
    
## Como la programacion es dinamica, tenemos que trabajar en funcion de que las estructuras de datos puedan cambiar
for i in range(0, len(a)):
    print(a(i))

# IF - Palabra reservada que se utiliza para hacer comparaciones
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

if a[0] == b[0]: #Si la expresion no es verdadera no entra en el if no se ejecuta, entra en el else...
    print("hola mundo")
else:
    print("hola codigo facilito")
    
    #Podemos evaluar las condiciones que queramos
if a[0] == b[0] and b[1] == a[1]: 
    print("hola mundo")
else:
    print("hola codigo facilito")
# WHILE - se usa mayormente con expresiones booleanas
# Hay que tener cuidado porque se corre el riesgo de tener un bucle infinito
i = 0
while i < len(a):
    print(a(i))
    i += 1 ## Este seria de cuanto en cuanto quiero incrementar
    
    
# DEF



# ELIF - (else if) - Es un shortcut para decir SI NO
#Obligatoriamente debe haber un IF ya que es la apertura de la condicion
#No es igual al else! SIEMPRE debe estar el elif antes que el else...
if a[0] == b[0]: 
    print("hola mundo")
elif b[1] == a[1]:
    print("hola codigo facilito")

# IMPORT


## Declaraciones de función (def)
## Declaraciones de importación (import).

a = [1, 2, 3, 4] ## Lista - se puede modificar (es mutable)
#Al ser mutable tiene una serie de metodos para poder manipularlas
# a.extend()
# a.pop()
# a.append()
# a.insert()
# a.sort()


b = (5, 6, 7, 8)  ## La tupla es inmutable, una vez declarada su valor no puede cambiar

## Diferencia entre Declaraciones y Expresiones

# Declaraciones: realizan acciones y controlan el flujo del programa
# Expresiones: producen valores

#Ejemplo:
# hacer una funcion que se llame divisibles_por_2
a = (5 , 2, 100, -2 , 30, 9999, -1111, 0 , 6)

def divisibles_por_2(data):
    divisibles = []
    for i in data:
        if i % 2 == 0:
            divisibles.append(i) ## El append añade elementos a la lista vacia
    return divisibles
print(divisibles_por_2(a))

#Libro: Fundamentos de la programacion editorial alfa omega


