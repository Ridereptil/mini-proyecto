import tkinter as tk
from views.activity import mostrar_actividades

def create_main_window():
    """Crea y configura la ventana principal"""
    window = tk.Tk()
    window.title("ToDo List App")
    window.geometry("500x300")
    
    # Mostrar el formulario de actividad al iniciar
    mostrar_actividades(window)
    
    return window