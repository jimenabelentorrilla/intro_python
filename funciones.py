# Crea un programa que pida el nombre y el año de nacimiento de un usuario y se calcule la edad del usuario y mostrar 
#un mensaje que diga "Bievenido al programa que calcula tu edad"
#"Hola," nombre, "Tu edad es: ", edad"
# Preguntar al usuario "Quieres salir? presiona s/n" si coloca
# s salir del programa si presiona n continuar ejecutando el programa.


def calcular_edad(nombre, anio_nac):
    anio_actual = 2024
    edad = anio_actual - int(anio_nac)   
    print(f"Hola,", nombre, "Tu edad es: ", edad) 
    
salir_o_no = "n"
while salir_o_no == "n":
    print("Bienvenido al programa que calcula tu edad")
    nombre = input("¿Cuál es tu nombre?: ")
    anio_nac = input("¿En que año naciste?: ")
    calcular_edad(nombre, anio_nac)
    salir_o_no = input("Quieres salir? Presiona s/n: ")
print("chau.")

## Calcular descuento - ejemplo

def calcular_descuento(precio, descuento):
    return (precio * descuento / 100)

descuento = calcular_descuento(1000, 50)

puntos = 10
total = descuento - puntos
print ("Total:", total)


    

