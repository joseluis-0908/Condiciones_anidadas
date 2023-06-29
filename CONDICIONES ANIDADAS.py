# Autor: Jose Luis Leal García
# Fecha: 29-06-2023
from datetime import date
hoy = date.today()
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE CLASES DE TRIANGULOS: ")
a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))
if a==b and b==c:
    print("***EL TRIANGULO ES EQUILATERO*** ")
else:
    if a==b or b==c or a==c:
        print("***EL TRIANGULO ES ISOCELES*** ")
    else:
        print("***EL TRIANGULO ES EQUILATERO***")
print()

animal = input("Digite un animal: ")
animal = animal.upper()

if animal == "PERRO ":
    print("Este animal es el mejor amigo del hombre: ", animal)
elif animal == "GATO":
    print("Este animal persigue a los ratones ", animal)
elif animal == "OSO":
    print("Este animal vive en el polonorte: ",animal)
else:
    print("No es perro, no es gato, no es oso... es: ", animal)
print()
print("*** FIN *** ")

