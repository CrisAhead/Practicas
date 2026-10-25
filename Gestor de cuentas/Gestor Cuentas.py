import sys
import json

try:
    with open("usuarios.json", "r") as archivo:
        lista_usuarios = json.load(archivo)
except FileNotFoundError:
    lista_usuarios = []

while True:
    opc = input("Ingrese una opción (1 para agregar usuario, 0 para salir): ")
    match opc:
        case "1":
            usuario = input("Ingrese su usuario: ")
            usuario_existe = False
            for u in lista_usuarios:
                if u["usuario"] == usuario:
                    usuario_existe = True
                    break
            if usuario_existe == True:
                print("Usuario ya existe.")
            else:
                contraseña = input("Ingrese su contraseña: ")
                usuario_nuevo = {"usuario": usuario, "contraseña": contraseña}
                lista_usuarios.append(usuario_nuevo)
                with open("usuarios.json", "w") as archivo:
                    json.dump(lista_usuarios, archivo, indent=4)
        case "0":
            print("Saliendo del programa.")
            sys.exit()
        case _:
            print("Opción no válida. Saliendo del programa.")
            sys.exit()


