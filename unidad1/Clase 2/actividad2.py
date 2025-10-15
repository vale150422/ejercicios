import tkinter as tk
import re
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("Prendas de Vestir")
ventana.geometry("400x550")

def validar_marca(*args):
    texto = var_marca.get()
    if texto and not texto.isalpha():
        lbl_error_marca.config(text="Solo se pueden escribir letras", fg="red")
    elif not texto:
        lbl_error_marca.config(text="Campo obligatorio", fg="red")
    else:
        lbl_error_marca.config(text="")

def validar_talla(*args):
    texto = var_talla.get()
    if texto and not texto.isdigit():
        lbl_error_talla.config(text="Solo se pueden escribir números", fg="red")
    elif not texto:
        lbl_error_talla.config(text="Campo obligatorio", fg="red")
    else:
        lbl_error_talla.config(text="")

def validar_valor(*args):
    texto = var_valor.get()

    if texto and not re.fullmatch(r"\d+(\.\d+)?", texto):
        lbl_error_valor.config(text="Solo números (puede usar .)", fg="red")
    elif not texto:
        lbl_error_valor.config(text="Campo obligatorio", fg="red")
    else:
        lbl_error_valor.config(text="")

def validar_fecha(*args):
    texto = var_fecha.get()

    if texto and not re.fullmatch(r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}", texto):
        lbl_error_fecha.config(text="Formato: dd-mm-aaaa o dd/mm/aaaa", fg="red")
    elif not texto:
        lbl_error_fecha.config(text="Campo obligatorio", fg="red")
    else:
        lbl_error_fecha.config(text="")

def validar_guardar():
    validar_marca()
    validar_talla()
    validar_valor()
    validar_fecha()

    if (lbl_error_marca.cget("text") or
        lbl_error_talla.cget("text") or
        lbl_error_valor.cget("text") or
        lbl_error_fecha.cget("text")):
        messagebox.showerror("Error", "Primero se deben corregir los campos en rojo")
        return

    messagebox.showinfo("Éxito", "Datos guardados correctamente")

titulo = tk.Label(ventana, text="Tema: Prenda de vestir", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

frame_campos = tk.Frame(ventana)
frame_campos.pack(pady=5)


tk.Label(frame_campos, text="Marca", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
var_marca = tk.StringVar()
var_marca.trace_add("write", validar_marca)
entry_marca = tk.Entry(frame_campos, textvariable=var_marca, width=25)
entry_marca.pack(padx=10, pady=2)
lbl_error_marca = tk.Label(frame_campos, text="", fg="red")
lbl_error_marca.pack(anchor="w", padx=10)


tk.Label(frame_campos, text="Talla", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
var_talla = tk.StringVar()
var_talla.trace_add("write", validar_talla)
entry_talla = tk.Entry(frame_campos, textvariable=var_talla, width=25)
entry_talla.pack(padx=10, pady=2)
lbl_error_talla = tk.Label(frame_campos, text="", fg="red")
lbl_error_talla.pack(anchor="w", padx=10)


tk.Label(frame_campos, text="Valor", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
var_valor = tk.StringVar()
var_valor.trace_add("write", validar_valor)
entry_valor = tk.Entry(frame_campos, textvariable=var_valor, width=25)
entry_valor.pack(padx=10, pady=2)
lbl_error_valor = tk.Label(frame_campos, text="", fg="red")
lbl_error_valor.pack(anchor="w", padx=10)


tk.Label(frame_campos, text="Fecha de Fabricación", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
var_fecha = tk.StringVar()
var_fecha.trace_add("write", validar_fecha)
entry_fecha = tk.Entry(frame_campos, textvariable=var_fecha, width=25)
entry_fecha.pack(padx=10, pady=2)
lbl_error_fecha = tk.Label(frame_campos, text="", fg="red")
lbl_error_fecha.pack(anchor="w", padx=10)

boton_guardar = tk.Button(
    ventana, text="Guardar", font=("Arial", 12, "bold"),
    bg="green", fg="white", command=validar_guardar
)
boton_guardar.pack(pady=20)

ventana.mainloop()