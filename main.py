import tkinter as tk
from tkinter import messagebox

# =========================
# CONFIGURACIÓN DE VENTANA
# =========================

# Crear ventana principal
ventana=tk.Tk()
# Título de la ventana
ventana.title("Lista de Tareas")
# Tamaño de la ventana
ventana.geometry("400x500")
entrada = tk.Entry(ventana, width=35)
entrada.pack(pady=10)
lista_tareas = tk.Listbox(ventana, width=45, height=15)
lista_tareas.pack(pady=10)

# =========================
# FUNCIONES (LÓGICA)
# =========================

# Función para agregar una tarea a la lista
def agregar_tarea():
    # Obtener el texto que el usuario escribió
    tarea = entrada.get()
    # Validar que no esté vacío
    if tarea.strip() == "":
        messagebox.showwarning("Advertencia", "Escribe una tarea")
    else:
        # Insertar tarea al final de la lista
        lista_tareas.insert(tk.END, tarea)
        # Limpiar el campo de texto
        entrada.delete(0, tk.END)

# Función para eliminar una tarea seleccionada
def eliminar_tarea():
    # Obtener la posición del elemento seleccionado
    seleccion = lista_tareas.curselection()
    # Verificar si hay selección
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")

# Función para limpiar toda la lista
def limpiar_lista():
    # Verificar si la lista tiene elementos
    if lista_tareas.size() > 0:
        lista_tareas.delete(0, tk.END)
    else:
        messagebox.showinfo("Información", "La lista ya esta vacía")


def marcar_completada():
    seleccion = lista_tareas.curselection()

    if seleccion:
        tarea = lista_tareas.get(seleccion[0])
        lista_tareas.delete(seleccion[0])
        lista_tareas.insert(seleccion[0], "✔ " + tarea)
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")

# Botón para agregar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Botón para eliminar tarea seleccionada
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Botón para limpiar toda la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

ventana.bind("<Return>", lambda event: agregar_tarea())

ventana.mainloop()
