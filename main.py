print("\t *Bienvenid@ a tu organizador de tareas* \n")

# Declaro e inicializo dos listas.
# En tasks se almacenarán las tareas y en marks, los recuadros.
tasks = []
marks = []
op = 0


# Función que muestra un listado (vacío o no) de tareas
def show_tasks(marks, tasks):
    if not tasks:
        print(" [ VACÍO ]")
    else:
        i = 0
        for task in tasks:
            marks.append("[ ]")
        for mark, task in zip(marks, tasks):
            i += 1
            print(mark, f"{i}-", task)


# Función que elimina una tarea de la lista
def delete_task(tasks, clave):
    clave -= 1
    tasks.pop(clave)
    return tasks


# Función que deja una "X" cuando la tarea es completada
def mark_completed(marks, clave):
    i = 0
    clave -= 1
    marks[clave] = "[X]"
    return marks


# Ciclo principal con menú de opciones (visible en cada iteración)
while op != 9:
    print("\n------------------------------------------")
    print(
        """Menú de opciones:
	1- Agregar tarea
 	2- Mostrar todas las tareas
	3- Eliminar una tarea
 	4- Marcar tareas completadas
	5- Borrar todo (¡CUIDADO! ACCION IRREVERSIBLE)
	9- Salir de la aplicación
	"""
    )
    print("------------------------------------------")
    op = int(input("\nTu elección: "))
    # Opción 1. Agrega una tarea
    if op == 1:
        print("\n\t- AGREGAR TAREA -")
        print("Ingresa una actividad")
        task = input("* ")
        tasks.append(task)
    # Op 2. Llama a la función show_tasks() para mostrar todas las tareas existentes
    elif op == 2:
        print("\n\t- TUS TAREAS -")
        show_tasks(marks, tasks)
    # Op 3. Muestra la lista de tareas, llama a la función delete_tasks() y muestra la lista actualizada
    elif op == 3:
        print("\n- Revisa el listado y elige el número que corresponde -")
        show_tasks(marks, tasks)
        index = int(input("¿Qué nro. de tarea quieres eliminar? "))
        delete_task(tasks, index)
        print("* ¡Elemento eliminado con éxito! *\n")
        print("\t- TUS TAREAS -\n **actualizado**")
        show_tasks(marks, tasks)
    # Op 4. Muestra la lista de tareas, llama a la función mark_completed() y muestra la lista actualizada
    elif op == 4:
        print("\n- Revisa el listado y elige el número que corresponde -")
        show_tasks(marks, tasks)
        index = int(input("\n¿Qué nro. de tarea completaste? "))
        mark_completed(marks, index)
        print("\n\t- TUS TAREAS - \n **actualizado**")
        show_tasks(marks, tasks)
    # Op 5. Vacía la lista de tareas y muestra el listado vacío.
    elif op == 5:
        tasks.clear()
        print("\n* Se eliminaron todas las tareas con éxito *")
        print("\n* TUS TAREAS *")
        show_tasks(marks, tasks)
    # Op 9. Con esta opción, el usuario finaliza el programa.
    elif op == 9:
        print("\t * Fin del programa *")
        break
    # Opción para ingresos erroneos o no listados.
    else:
        print("Opción fuera de rango")
