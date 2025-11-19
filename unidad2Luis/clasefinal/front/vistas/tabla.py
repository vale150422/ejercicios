# vistas/tabla.py
import tkinter as tk
from tkinter import ttk

class Tabla:
    def __init__(self, master, titulos, columnas, data):
        self.columnas = columnas
        # creamos el Treeview dentro del master pasado (puede ser un Frame)
        self.tabla = ttk.Treeview(master, columns=self.columnas, show='headings')
        # headings
        for i, col in enumerate(self.columnas):
            self.tabla.heading(col, text=titulos[i])
            self.tabla.column(col, width=120, anchor='w')
        # cargar inicial
        self.refrescar(data)

    def refrescar(self, data):
        # limpia
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # inserta
        for fila in data:
            # fila debe coincidir con el orden de columnas
            self.tabla.insert('', 'end', values=fila)

