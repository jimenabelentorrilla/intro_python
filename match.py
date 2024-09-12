## La declaracion match-case es una nueva caracteristica de Python 3.10 que proporciona una forma concisa y expresiva de realizar coincidencias de patrones en estructuras de datos.
## Parecido a un switch, o a tener muchos IF

#match expression:
#    case pattern1:
        #Codigo a ejecutar si se cumple el patron1
#    case pattern2:
        #Codigo a ejecutar si se cumple el patron2
#    case _:
        #Codigo a ejecutar si no se cumple ningun patron
        
        
# Match Case - Ejemplo de validación

## Creamos una funcion que retorne un diccionario para luego llamarla cuando lo necesite, en este caso acceder al usuario y contraseña si es que tiene acceso a la base de datos
def provide_access(user):
    return {
        "username": user,
        "password": "admin"
    }

user = str(input("Escribe tu usuario: "))

match user:
    case "Ana":
        print("Ana no tiene acceso a la base de datos, solo tiene acceso al backend.")
    case "Carlos":
        print("Carlos no tiene acceso a la base de datos, solo tiene acceso al frontend.")
    case "Caro":
        print("Caro tiene acceso a la base de datos")
        print(provide_access(user))
    case _:
        print("No tienes acceso al sistema.")    
        

## Ejemplo con el OR ( | )

match user:
    case "Ana" | "Carlos":
        print("No tienes acceso a la base de datos.")
    case "Caro":
        print("Caro tiene acceso a la base de datos")
        print(provide_access(user))
    case _:
        print("No tienes acceso al sistema.")   
        
        
## Ejemplo usando expresión compleja

#Hacemos una lista de los usuarios que tienen acceso al sistema
allowed_users = ["caro", "ana"]

match user:
    #Si el usuario esta dentro de esta lista... entonces retorna usuario
    case user if user in allowed_users:
        print(f"{user} tiene acceso a la base de datos")
        print(provide_access(user))
    case _:
        print("No tienes acceso al sistema")