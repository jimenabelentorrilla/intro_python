## Realizar una funcion que retorne todos los numeros primos
#  entre 1 y un numero x que debe recibir por parametro y luego imprimir esos numeros

def numeros_primos(x):
    primos = []
    
    for num in range(2, x + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    
    return primos

# Ejemplo de uso
x = 20  # Puedes cambiar este valor por el número que desees
print(numeros_primos(x))

## Explicación:

# Rango de números: La función itera desde 2 hasta el número x (inclusive).
# Verificación de primos: Para cada número num, se verifica si es divisible por algún número entre 2 y la raíz cuadrada de num. Si encuentra un divisor, es_primo se marca como False, y el ciclo se rompe.
# Lista de primos: Si el número es primo, se agrega a la lista primos.
# Devolución: Finalmente, la función retorna la lista de números primos.
# Este código imprimirá todos los números primos entre 1 y x. Por ejemplo, para x = 20, la salida será [2, 3, 5, 7, 11, 13, 17, 19].
