import tkinter as tk
import re
from tkinter import messagebox
from modelos.almacen import Almacen
from controladores.comunicacion import Comunicacion
from vistas.tabla import Tabla


class Interfaz():

    @staticmethod
    def mostrar_interfaz():
        ventana = tk.Tk()
        almacen = Almacen(ventana)
        comunicacion = Comunicacion()

        ventana.title("Prendas de Vestir")
        ventana.geometry("480x700")

        # Título de la ventana
        titulo = tk.Label(ventana, text="Prendas de Vestir", font=("Arial", 15, "bold"))
        titulo.pack(pady=5)

        # Campo ID
        tk.Label(ventana, text="ID", font=("Arial", 11)).pack(anchor="w", padx=10)
        var_id = tk.StringVar()
        entry_id = tk.Entry(ventana, textvariable=var_id, width=25)
        entry_id.pack(padx=10)
        lbl_error_id = tk.Label(ventana, text="", fg="red")
        lbl_error_id.pack(anchor="w", padx=10)

        # Función para crear campos con etiqueta y error
        def crear_campo(nombre, variable):
            tk.Label(ventana, text=nombre, font=("Arial", 11)).pack(anchor="w", padx=10)
            entry = tk.Entry(ventana, textvariable=variable, width=25)
            entry.pack(padx=10)
            lbl = tk.Label(ventana, text="", fg="red")
            lbl.pack(anchor="w", padx=10)
            return entry, lbl

        # Campos de la prenda
        entry_marca, lbl_error_marca = crear_campo("Marca", almacen.var_marca)
        entry_talla, lbl_error_talla = crear_campo("Talla", almacen.var_talla)
        entry_valor, lbl_error_valor = crear_campo("Valor", almacen.var_valor)
        entry_fecha, lbl_error_fecha = crear_campo("Fecha de Fabricación", almacen.var_fecha_fabricacion)

        # Funciones de validación de cada campo
        def validar_marca(*a):
            t = almacen.var_marca.get()
            if t == "":
                lbl_error_marca.config(text="Campo obligatorio")
            elif not t.isdigit() and not t.isalpha():
                lbl_error_marca.config(text="ID o texto inválido")
            else:
                lbl_error_marca.config(text="")

        def validar_talla(*a):
            t = almacen.var_talla.get()
            if t == "":
                lbl_error_talla.config(text="Campo obligatorio")
            elif not re.fullmatch(r"[A-Za-z0-9]+", t):
                lbl_error_talla.config(text="No símbolos")
            else:
                lbl_error_talla.config(text="")

        def validar_valor(*a):
            t = almacen.var_valor.get()
            if t == "":
                lbl_error_valor.config(text="Campo obligatorio")
            elif not re.fullmatch(r"\d+(\.\d+)?", t):
                lbl_error_valor.config(text="Solo números")
            else:
                lbl_error_valor.config(text="")

        def validar_fecha(*a):
            t = almacen.var_fecha_fabricacion.get()
            if t == "":
                lbl_error_fecha.config(text="Campo obligatorio")
            elif not re.fullmatch(r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}", t):
                lbl_error_fecha.config(text="Formato: dd-mm-aaaa")
            else:
                lbl_error_fecha.config(text="")

        # Función para actualizar la tabla con todos los registros
        def actualizar_tabla():
            registros = comunicacion.consultar_todo()
            data = [(r["id"], r["marca"], r["talla"], r["valor"], r["fecha"]) for r in registros]
            tabla.refrescar(data)

        # Guardar o actualizar un registro
        def guardar():
            validar_marca()
            validar_talla()
            validar_valor()
            validar_fecha()

            # Revisar si hay errores
            if (lbl_error_marca.cget("text") or lbl_error_talla.cget("text") or
                lbl_error_valor.cget("text") or lbl_error_fecha.cget("text")):
                messagebox.showerror("Error", "Corrige los campos en rojo")
                return

            id_existente = var_id.get()

            # Actualizar si hay un ID válido
            if id_existente.isdigit():
                resultado = comunicacion.actualizar(
                    id_existente,
                    almacen.var_marca.get(),
                    almacen.var_talla.get(),
                    almacen.var_valor.get(),
                    almacen.var_fecha_fabricacion.get()
                )

                if resultado:
                    messagebox.showinfo("Éxito", "Registro actualizado correctamente")
                else:
                    messagebox.showerror("Error", "El ID no existe")
                    return

            # Guardar nuevo registro si no hay ID
            else:
                comunicacion.guardar(
                    almacen.var_marca.get(),
                    almacen.var_talla.get(),
                    almacen.var_valor.get(),
                    almacen.var_fecha_fabricacion.get()
                )
                messagebox.showinfo("Éxito", "Guardado correctamente")

            actualizar_tabla()

            # Limpiar campos
            var_id.set("")
            almacen.var_marca.set("")
            almacen.var_talla.set("")
            almacen.var_valor.set("")
            almacen.var_fecha_fabricacion.set("")

        # Consultar un registro por ID
        def consultar_uno():
            id_buscar = var_id.get()

            if not id_buscar.isdigit():
                messagebox.showerror("Error", "Debes escribir un ID válido en el campo ID")
                return

            r = comunicacion.consultar(id_buscar)

            if "error" in r:
                messagebox.showinfo("Aviso", r["error"])
                return

            # Rellenar los campos con los datos
            var_id.set(r["id"])
            almacen.var_marca.set(r["marca"])
            almacen.var_talla.set(r["talla"])
            almacen.var_valor.set(r["valor"])
            almacen.var_fecha_fabricacion.set(r["fecha"])

            # Mostrar solo este registro en la tabla
            tabla.refrescar([
                (r["id"], r["marca"], r["talla"], r["valor"], r["fecha"])
            ])

        # Función para borrar registro seleccionado
        def borrar():
            seleccion = tabla.tabla.selection()
            if not seleccion:
                messagebox.showerror("Error", "Debes seleccionar un registro en la tabla.")
                return

            item = seleccion[0]
            valores = tabla.tabla.item(item)["values"]
            id_eliminar = valores[0]

            # Eliminar del controlador y de la tabla
            comunicacion.eliminar(id_eliminar)
            tabla.tabla.delete(item)

            messagebox.showinfo("Éxito", "Registro eliminado correctamente")

        # Botones de acción
        frame_botones = tk.Frame(ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Guardar", width=12, command=guardar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Consultar 1", width=12, command=consultar_uno).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Consultar todos", width=15, command=actualizar_tabla).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Borrar", width=12, command=borrar).grid(row=0, column=3, padx=5)

        # Tabla de registros
        frame_tabla = tk.Frame(ventana)
        frame_tabla.pack(fill="both", expand=True, pady=10)

        titulos = ["ID", "Marca", "Talla", "Valor", "Fecha"]
        columnas = ["id", "marca", "talla", "valor", "fecha"]

        tabla = Tabla(frame_tabla, titulos, columnas, [])
        tabla.tabla.pack(fill="both", expand=True)

        # Asociar validaciones a las teclas
        entry_marca.bind("<KeyRelease>", validar_marca)
        entry_talla.bind("<KeyRelease>", validar_talla)
        entry_valor.bind("<KeyRelease>", validar_valor)
        entry_fecha.bind("<KeyRelease>", validar_fecha)

        ventana.mainloop()
