import tkinter as tk 


class Almacen():

    def __init__(self, ventanaprincipal):

        self.ventanaprincipal = ventanaprincipal
        self.marca = tk.StringVar(ventanaprincipal)
        self.talla = tk.StringVar(ventanaprincipal)
        self.valor = tk.StringVar(ventanaprincipal)
        self.fecha_fabricacion = tk.StringVar(ventanaprincipal)

        self.ventanaprincipal = ventanaprincipal
        self.var_marca = tk.StringVar(ventanaprincipal)
        self.var_talla = tk.StringVar(ventanaprincipal)
        self.var_valor = tk.StringVar(ventanaprincipal)
        self.var_fecha_fabricacion = tk.StringVar(ventanaprincipal)

        self.arr_marca = tk.StringVar(ventanaprincipal)
        self.arr_talla = tk.StringVar(ventanaprincipal)
        self.arr_valor = tk.StringVar(ventanaprincipal)
        self.arr_fecha_fabricacion = tk.StringVar(ventanaprincipal)