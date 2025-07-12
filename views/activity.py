import tkinter as tk
from tkinter import ttk, messagebox
from db.operations import guardar_actividad, obtener_actividades
from views.resources import PRIMARY_COLOR, SECUNDARY_COLOR, THIRD_COLOR, TITLE, TEXT, FOURTH_COLOR

def mostrar_actividades(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    
    ventana.configure(bg=FOURTH_COLOR)
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(1, weight=1)

    formulario_frame = tk.Frame(ventana, bg=FOURTH_COLOR, padx=20, pady=20)
    formulario_frame.grid(row=0, column=0, sticky="ew")



    tk.Label(formulario_frame, text="Nueva Actividad", font=TITLE, bg=FOURTH_COLOR,fg=SECUNDARY_COLOR).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(formulario_frame, text="Título:", font=TEXT, bg=FOURTH_COLOR,fg=PRIMARY_COLOR).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    
    tk.Entry(formulario_frame, textvariable=tk.StringVar, width=40, font=TEXT,bg="white",fg="black").grid(row=1, column=1, padx=5, pady=5)

    tk.Label(formulario_frame, text="Descripción:", font=TEXT, bg=FOURTH_COLOR,fg=PRIMARY_COLOR).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    
    tk.Entry(formulario_frame, textvariable=tk.StringVar(), width=40, font=TEXT,bg="white",fg="black").grid(row=2, column=1, padx=5, pady=5)

    def guardar():
        if not tk.StringVar.get().strip() or not tk.StringVar.get().strip():
            messagebox.showerror("Error", "Debes llenar ambos campos")
            return
            
        if guardar_actividad({
            "title": tk.StringVar.get().strip(),
            "description": tk.StringVar.get().strip()
        }):
            messagebox.showinfo("Éxito", "Actividad guardada correctamente")
            tk.StringVar.set("")
            tk.StringVar.set("")
            actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo guardar la actividad")

    tk.Button(formulario_frame, text="Guardar", command=guardar, bg=THIRD_COLOR,fg="white", font=TEXT,relief="flat",padx=20).grid(row=3, column=1, pady=10, sticky="e")

    tabla_frame = tk.Frame(ventana, bg=FOURTH_COLOR)
    tabla_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))

    tk.Label(tabla_frame, text="Lista de Actividades", font=TITLE, bg=FOURTH_COLOR,fg=SECUNDARY_COLOR).pack(pady=(0, 10))

    style = ttk.Style()
    style.configure("Treeview", font=TEXT,background="white",fieldbackground="white")
    style.configure("Treeview.Heading", font=TEXT,background=PRIMARY_COLOR,foreground="white")

    tabla = ttk.Treeview(tabla_frame, columns=("id", "titulo", "descripcion", "fecha"), show="headings")
    tabla.heading("id", text="ID")
    tabla.heading("titulo", text="Título")
    tabla.heading("descripcion", text="Descripción")
    tabla.heading("fecha", text="Fecha")

    tabla.column("id", width=50, anchor="center")
    tabla.column("titulo", width=150)
    tabla.column("descripcion", width=250)
    tabla.column("fecha", width=120, anchor="center")

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tabla.pack(fill="both", expand=True)

    def actualizar_tabla():
        for item in tabla.get_children():
            tabla.delete(item)
        
        actividades = obtener_actividades()
        for actividad in actividades:
            tabla.insert("", "end", values=actividad)

    actualizar_tabla()