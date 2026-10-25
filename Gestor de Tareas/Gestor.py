def ver():
    for i in tareas:
        print(f"{i['nombre']}, Completado: {i['completada']}")

def agregar(tareas2):
    tareas2.append({"nombre" : input("ingrese nombre de la tarea: "), "completada" : False})

def marcar(tareas2):
    nombre = input("ingrese nombre de la tarea a marcar: ")
    for i in tareas2:
        if i["nombre"] == nombre:
            i["completada"] = True
            print("Tarea Completada")
            return
    print("nombre no existe")

def eliminar(tareas2):
    nombre = input("ingrese nombre de la tarea a borrar: ")
    for i in tareas2:
        if i["nombre"] == nombre:
            tareas2.remove(i)
            print("eliminado correctamente")
            return
    print("No se encontro la tarea.")

#------------------------------------------------Main
tareas = []

archivo = open("tareas.txt", "r")
for linea in archivo:
    nombre, completada = linea.strip().split(",")
    tareas.append({
        "nombre": nombre,
        "completada": completada == "True"
    })

archivo.close()


while(True):
    print("1_Ver Tareas\n"
          "2_Agregar Tarea\n"
          "3_Marcar Completada\n"
          "4_Eliminar Tarea\n"
          "5_Salir")

    opc = input("Ingrese una opción: ")

    match opc:
        case "1":
            ver()
        case "2":
            agregar(tareas)
        case "3":
            marcar(tareas)
        case "4":
            eliminar(tareas)
        case "5":
            archivo = open("tareas.txt", "w")
            for tarea in tareas:
                archivo.write(f"{tarea['nombre']},{tarea['completada']}\n")
            archivo.close()
            break
        case _:
            print("ERROR")

