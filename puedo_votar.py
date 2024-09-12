##Escribe una expresion booleana que verifique si un numero es par.
numero = input("Digite un numero: ")

if int(numero) % 2 == 0:
    print("El numero " + str(numero) + " es par")
else:
    print ("NO ES PAR")
    

##Crea una expresion booleana que compruebe si una cadena tiene al menos 10 caracteres.
contra = "Chumino123"
nueva_contra = input("Escribe su contraseña: ")
pin_recuperacion = 123

if (str(contra) == str(nueva_contra)) and len(nueva_contra) >= 10:
    print("Su contraseña es correcta, bienvenido")
    cambio_contra = input("Por favor cambie su contraseña: ")
    if (str(nueva_contra) == str(cambio_contra)):
        print("Su contraseña es la misma")
    else:
        if len(cambio_contra) > 10:
            contra = nueva_contra
            print("Perfecto! Tu nueva contraseña es: ", cambio_contra)
        else:
            print("La contraseña debe tener mas de 10 caracteres")
else:
    print("Contraseña incorrecta")
    pin = int(input("Digite su pin de recuperacion: "))
    if (pin_recuperacion == pin):
        print("Ha recuperado su cuenta con exito!")
    else:
        print("No puedes ingresar.")


##Escribe una expresion que evalue si una persona es elegible para votar en funcion de su edad
## (por ejemplo, si tienen 18 o mas).

edad = input("Digame su EDAD!!: ")
mayoria_edad = 18

if (int(edad) >= int(mayoria_edad)):
    print("Tiene la posibilidad de votar!")
else:
    print("No podes votar sos menor!")