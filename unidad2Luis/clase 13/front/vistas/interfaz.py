import tkinter as tk
import re
from tkinter import Label, messagebox
from modelos.almacen import Almacen
from controladores.validacion import Validaciones
from controladores.comunicacion import Comunicacion


class Interfaz():

    def mostrar_interfaz():
        ventana = tk.Tk()
        almacen = Almacen(ventana)
        comunicacion = Comunicacion()  # 🔹 Nueva: conexión con el backend Django

        ventana.title("Prendas de Vestir")
        ventana.geometry("400x550")

        titulo = tk.Label(ventana, text="Tema: Prenda de vestir", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        # ────────────────────────────── CAMPOS ──────────────────────────────
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

        # ────────────────────────────── VALIDACIONES ──────────────────────────────
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
            if texto and not re.fullmatch(r"[A-Za-z0-9]+", texto):  # 🔹 Mejora: permite letras y números
                lbl_error_talla.config(text="No se permiten /-.,", fg="red")
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

        # ────────────────────────────── GUARDAR ──────────────────────────────
        def validar_guardar():
            validar_marca()
            validar_talla()
            validar_valor()
            validar_fecha()

            # Si hay errores en los campos
            if (lbl_error_marca.cget("text") or
                lbl_error_talla.cget("text") or
                lbl_error_valor.cget("text") or
                lbl_error_fecha.cget("text")):
                messagebox.showerror("Error", "Primero se deben corregir los campos en rojo")
                return

            # Enviar al backend
            exito = comunicacion.guardar(
                almacen.var_marca.get(),
                almacen.var_talla.get(),
                almacen.var_valor.get(),
                almacen.var_fecha_fabricacion.get()
            )

            if exito:
                messagebox.showinfo("Éxito", "Datos guardados en el servidor correctamente")
                # Limpia los campos después de guardar
                almacen.var_marca.set("")
                almacen.var_talla.set("")
                almacen.var_valor.set("")
                almacen.var_fecha_fabricacion.set("")
            else:
                messagebox.showerror("Error", "No se pudo conectar con el servidor")

        # ────────────────────────────── BOTÓN GUARDAR ──────────────────────────────
        boton_guardar = tk.Button(
            ventana, text="Guardar", font=("Arial", 12, "bold"),
            bg="green", fg="white", command=validar_guardar
        )
        boton_guardar.pack(pady=20)

        # ────────────────────────────── BINDEOS CORRECTOS ──────────────────────────────
        entry_marca.bind('<KeyRelease>', validar_marca)
        entry_talla.bind('<KeyRelease>', validar_talla)
        entry_valor.bind('<KeyRelease>', validar_valor)
        entry_fecha.bind('<KeyRelease>', validar_fecha)

        ventana.mainloop()
