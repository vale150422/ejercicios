import tkinter as tk
from tkinter import messagebox
import re

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Ventana Principal")
ventanaPrincipal.geometry("300x300")
def validarTexto(texto):
   
    patron = re.compile("^[A-Za-z ]*$")
    return patron.match(texto) is not None

def devolverCaracter(texto):
    if not validarTexto(texto):
        return False
    return True

def guardar():
    tipo = entryTipo.get()
    valor = entryValor.get()
    autor = entryAutor.get()
    fecha = entryFecha.get()
    
    if not tipo or not valor or not autor or not fecha:
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
        return
    
    
    mensaje = f"Dibujo guardado:\n\nTipo: {tipo}\nValor: {valor}\nAutor: {autor}\nFecha: {fecha}"
    messagebox.showinfo("Guardado", mensaje)

def salir():
    ventanaPrincipal.destroy()


ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Registro de Dibujo")
ventanaPrincipal.geometry("350x350")


labelTipo = tk.Label(ventanaPrincipal, text="Tipo de Dibujo")
labelTipo.pack()
entryTipo = tk.Entry(ventanaPrincipal)
entryTipo.pack()

labelValor = tk.Label(ventanaPrincipal, text="Valor")
labelValor.pack()
entryValor = tk.Entry(ventanaPrincipal)
entryValor.pack()

labelAutor = tk.Label(ventanaPrincipal, text="Autor")
labelAutor.pack()
entryAutor = tk.Entry(ventanaPrincipal, validate="key")
entryAutor['validatecommand'] = (entryAutor.register(devolverCaracter), '%P')
entryAutor.pack()

labelFecha = tk.Label(ventanaPrincipal, text="Fecha de Realización")
labelFecha.pack()
entryFecha = tk.Entry(ventanaPrincipal)
entryFecha.pack()


btnGuardar = tk.Button(ventanaPrincipal, text="Guardar", command=guardar, bg="lightgreen")
btnGuardar.pack(pady=10)

btnSalir = tk.Button(ventanaPrincipal, text="Salir", command=salir, bg="lightcoral")
btnSalir.pack()

ventanaPrincipal.mainloop()