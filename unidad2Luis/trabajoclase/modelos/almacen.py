import tkinter as tk 


class almacen():

    def __init__(self, ventanaprincipal, marca, talla, valor, fecha_fabricacion):

        self.ventanaprincipal = ventanaprincipal
        self.marca = tk.StringVar(ventanaprincipal)
        self.talla = tk.StringVar(ventanaprincipal)
        self.valor = tk.StringVar(ventanaprincipal)
        self.fecha_fabricacion = tk.StringVar(ventanaprincipal)