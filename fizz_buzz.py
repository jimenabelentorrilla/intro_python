##Ejemplo fizzbuzz

##Escriba un programa que imprima los numeros del 1 al 100
#Si el numero es multiplo de 3 imprimir Fizz
#Si el numero es multiplo de 5 imprimir Buzz
#Si el numero es multiplo de 3 y 5 imprimir FizzBuzz

num = 0  

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} -> FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} -> Fizz")
    elif i % 5 == 0:
        print (f"{i} -> Buzz")
    else:
        print(f"{i}")
    num += 1    

# Tarea:

# Hacer el mismo ejercicio usando WHILE

num = 1

while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} -> FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} -> Fizz")
    elif num % 5 == 0:
        print (f"{num} -> Buzz")
    else:
        print(f"{num}")
    num += 1

