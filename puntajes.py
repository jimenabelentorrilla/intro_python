score = float(input("Ingresa tu puntaje en numeros: "))

if 4.5 <= score <= 5: 
    grade = "E"
elif 4 <= score < 4.5:
    grade = "S"
elif 3 <= score < 4:
    grade = "A"
elif 2 <= score < 3:
    grade = "I"
elif 0 <= score < 2:
    grade = "D"
else: 
    grade = "Puntaje inválido"
    
##Diccionarios - llave valor y puedo acceder a los valores por medio de las llaves

grades = {
    "E": "Excelente",
    "S": "Sobresaliente",
    "A": "Aprobado",
    "I": "Insuficiente",
    "D": "Deficiente",
}
## Tenemos que acceder al valor para eso utilizamos una funcion llamada .GET
## Si la llave no existe, retorna NONE y si existe retorna TRUE.

print(f"Tu puntaje es --> {grade}: {grades.get(grade) or ''}")

