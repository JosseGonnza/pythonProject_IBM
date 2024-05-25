import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, ventana):
        """Inicializa la aplicación de lista de tareas."""
        self.ventana = ventana
        self.ventana.title("Lista de tareas")
        self.ventana.geometry("400x400")  # Establece el tamaño de la ventana

        # Entrada de texto para nuevas tareas
        self.entrada_tarea = tk.Entry(ventana, font=("Arial", 14), width=30)
        self.entrada_tarea.pack(pady=10)  # Añade padding vertical para espaciado

        # Botón para agregar tareas a la lista
        self.boton_agregar = tk.Button(ventana, text="Agregar tarea", font=("Arial", 12), command=self.agregar_tarea, width=20)
        self.boton_agregar.pack(pady=5)  

        # Lista para mostrar las tareas
        self.lista_tareas = tk.Listbox(ventana, font=("Arial", 12), width=40, height=10)
        self.lista_tareas.pack(pady=10)  

        # Botón para marcar tareas como completadas
        self.boton_completar = tk.Button(ventana, text="Marcar como completada", font=("Arial", 12), command=self.marcar_como_completada, width=20)
        self.boton_completar.pack(pady=5)  

        # Botón para eliminar tareas seleccionadas
        self.boton_eliminar = tk.Button(ventana, text="Eliminar tarea", font=("Arial", 12), command=self.eliminar_tarea, width=20)
        self.boton_eliminar.pack(pady=5)  

    def agregar_tarea(self):
        """Agrega una nueva tarea a la lista."""
        tarea = self.entrada_tarea.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Limpia la entrada de texto después de agregar la tarea
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")  # Muestra una advertencia si la entrada está vacía

    def marcar_como_completada(self):
        """Marca la tarea seleccionada como completada."""
        try:
            seleccion = self.lista_tareas.curselection()  # Obtiene la selección actual
            if seleccion:
                tarea = self.lista_tareas.get(seleccion)
                if "(Completada)" in tarea:
                    messagebox.showwarning("Advertencia", "La tarea ya está completada")  # Advertencia si la tarea ya está completada
                else:
                    self.lista_tareas.delete(seleccion)  # Elimina la tarea de la lista
                    self.lista_tareas.insert(seleccion, f"{tarea} (Completada)")  # Inserta la tarea como completada
            else:
                messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada")  # Advertencia si no hay selección
        except IndexError:
            messagebox.showerror("Error", "No se pudo marcar la tarea como completada")  # Error si ocurre un problema

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            seleccion = self.lista_tareas.curselection()  # Obtiene la selección actual
            if seleccion:
                self.lista_tareas.delete(seleccion)  # Elimina la tarea seleccionada
            else:
                messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")  # Advertencia si no hay selección
        except IndexError:
            messagebox.showerror("Error", "No se pudo eliminar la tarea")  # Error si ocurre un problema

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
app = ListaTareasApp(ventana)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
