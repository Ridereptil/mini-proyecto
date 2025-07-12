import tkinter as tk
from views.activity import mostrar_actividades

def create_main_window():
    window = tk.Tk()
    window.title("ToDo List App")
    window.geometry("1000x600")
    
    mostrar_actividades(window)
    
    return window