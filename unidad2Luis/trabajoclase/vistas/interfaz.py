import tkinter as tk
import re
from tkinter import Label
from tkinter import messagebox
from modelos.almacen import Almacen
from controladores.validacion import Validaciones


class Interfaz():

    def mostrar_interfaz():

        ventana = tk.Tk()
        almacen = Almacen(ventana)
        ventana.title("Prendas de Vestir")
        ventana.geometry("400x550")

        titulo = tk.Label(ventana, text="Tema: Prenda de vestir", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        def evento_presionar_tecla(evento):

            #marca
            if Validaciones.validar_letras(almacen.marca):
                almacen.arr_marca.set("")
            else:
                almacen.arr_marca.set("solo se pueden escribir letras")
            
            #talla
            if Validaciones.validar_letrasynumeros(almacen.talla):
                almacen.arr_talla.set("")
            else:
                almacen.arr_talla.set("no se permiten /-,.")

            #valor
            if Validaciones.validar_numeros(almacen.valor):
                almacen.arr_valor.set("")
            else:
                almacen.arr_valor.set("solo numeros(puede usar .)")

            #fecha fabricacion
            if Validaciones.validar_numeros(almacen.fecha_fabricacion):
                almacen.arr_fecha_fabricacion.set("")
            else:
                almacen.arr_fecha_fabricacion.set("Formato: dd-mm-aaaa o dd/mm/aaaa")


        tk.Label(ventana, text="Marca", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
        entry_marca = tk.Entry(ventana, textvariable=almacen.var_marca, width=25)
        entry_marca.pack(padx=10, pady=2)
        lbl_error_marca = tk.Label(ventana, text="", fg="red")
        lbl_error_marca.pack(anchor="w", padx=10)


        tk.Label(ventana, text="Talla", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
        entry_talla = tk.Entry(ventana, textvariable=almacen.var_talla, width=25)
        entry_talla.pack(padx=10, pady=2)
        lbl_error_talla = tk.Label(ventana, text="", fg="red")
        lbl_error_talla.pack(anchor="w", padx=10)


        tk.Label(ventana, text="Valor", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
        entry_valor = tk.Entry(ventana, textvariable=almacen.var_valor, width=25)
        entry_valor.pack(padx=10, pady=2)
        lbl_error_valor = tk.Label(ventana, text="", fg="red")
        lbl_error_valor.pack(anchor="w", padx=10)


        tk.Label(ventana, text="Fecha de Fabricación", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
        entry_fecha = tk.Entry(ventana, textvariable=almacen.var_fecha_fabricacion, width=25)
        entry_fecha.pack(padx=10, pady=2)
        lbl_error_fecha = tk.Label(ventana, text="", fg="red")
        lbl_error_fecha.pack(anchor="w", padx=10)


        def validar_marca(*args):
            texto = almacen.var_marca.get()
            if texto and not texto.isalpha():
                lbl_error_marca.config(text="Solo se pueden escribir letras", fg="red")
            elif not texto:
                lbl_error_marca.config(text="Campo obligatorio", fg="red")
            else:
                lbl_error_marca.config(text="")

        def validar_talla(*args):
            texto = almacen.var_talla.get()
            if texto and not texto.isdigit():
                lbl_error_talla.config(text="no se permiten /-.,", fg="red")
            elif not texto:
                lbl_error_talla.config(text="Campo obligatorio", fg="red")
            else:
                lbl_error_talla.config(text="")

        def validar_valor(*args):
            texto = almacen.var_valor.get()

            if texto and not re.fullmatch(r"\d+(\.\d+)?", texto):
                lbl_error_valor.config(text="Solo números (puede usar .)", fg="red")
            elif not texto:
                lbl_error_valor.config(text="Campo obligatorio", fg="red")
            else:
                lbl_error_valor.config(text="")

        def validar_fecha(*args):
            texto = almacen.var_fecha_fabricacion.get()
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



        
        boton_guardar = tk.Button(
            ventana, text="Guardar", font=("Arial", 12, "bold"),
            bg="green", fg="white", command=validar_guardar
        )
        boton_guardar.pack(pady=20)

        entry_marca.bind('<KeyRelease>', validar_marca)
        entry_talla.bind('<KeyRelease>', validar_marca)
        entry_valor.bind('<KeyRelease>', validar_valor)
        entry_fecha.bind('<KeyRelease>', validar_fecha)
        

        ventana.mainloop()