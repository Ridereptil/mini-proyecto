import tkinter as tk
from tkinter import ttk, messagebox
from db.operations import guardar_actividad, obtener_actividades

def mostrar_actividades(ventana):
    # Limpiar ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Configurar grid
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(1, weight=1)

    # Frame para el formulario
    formulario_frame = tk.Frame(ventana, padx=10, pady=10)
    formulario_frame.grid(row=0, column=0, sticky="ew")

    # Variables del formulario
    titulo_var = tk.StringVar()
    descripcion_var = tk.StringVar()

    # Campos del formulario
    tk.Label(formulario_frame, text="Título:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    tk.Entry(formulario_frame, textvariable=titulo_var, width=40).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(formulario_frame, text="Descripción:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    tk.Entry(formulario_frame, textvariable=descripcion_var, width=40).grid(row=1, column=1, padx=5, pady=5)

    def guardar_actividad_handler():
        """Maneja el guardado de actividades"""
        if not titulo_var.get().strip() or not descripcion_var.get().strip():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
            
        if guardar_actividad({
            "title": titulo_var.get().strip(),
            "description": descripcion_var.get().strip()
        }):
            messagebox.showinfo("Éxito", "Actividad guardada correctamente")
            titulo_var.set("")
            descripcion_var.set("")
            actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo guardar la actividad")

    tk.Button(formulario_frame, text="Guardar", command=guardar_actividad_handler).grid(row=2, column=1, pady=10)

    # Frame para la tabla
    tabla_frame = tk.Frame(ventana)
    tabla_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    # Crear Treeview
    tabla = ttk.Treeview(tabla_frame, columns=("id", "titulo", "descripcion", "fecha"), show="headings")
    tabla.heading("id", text="ID")
    tabla.heading("titulo", text="Título")
    tabla.heading("descripcion", text="Descripción")
    tabla.heading("fecha", text="Fecha de Registro")

    # Configurar columnas
    tabla.column("id", width=50, anchor="center")
    tabla.column("titulo", width=150)
    tabla.column("descripcion", width=250)
    tabla.column("fecha", width=120, anchor="center")

    # Scrollbar
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tabla.pack(fill="both", expand=True)

    def actualizar_tabla():
        """Actualiza la tabla con todas las actividades"""
        # Limpiar tabla
        for item in tabla.get_children():
            tabla.delete(item)
        
        # Obtener y mostrar todas las actividades
        actividades = obtener_actividades()
        for actividad in actividades:
            tabla.insert("", "end", values=actividad)

    # Mostrar actividades al iniciar
    actualizar_tabla()