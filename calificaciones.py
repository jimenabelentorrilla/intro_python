##Ejercicio

#Crea un programa que pida 5 calificaciones y mostrar un arreglo con 
#las calificciones y el promedio de ess calificaciones

#Calificaciones: [8,9,10,10,8]
#Promedio: 9.0


calificaciones = []
suma = 0
    
for i in range(5):
    calificacion = input("Dame una calificacion: ")
    calificaciones.append(calificacion)
    suma += int(calificacion)
promedio = suma / len(calificaciones)
print(calificaciones)
print(f"El promedio es:", promedio)

