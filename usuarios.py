cuantos = int(input("Ingrese la cantidad de usuarios que desea registrar: "))

usuarios = []
for i in range(cuantos):
    nombre  = input("Ingrese el nombre del usuario: ")
    usuarios.append(nombre)
    