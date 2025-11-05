import tkinter as tk
from tkinter.messagebox import askyesno, showerror, showinfo
from controladores.validadores import Validaciones  # Asegúrate de que exista esta clase


class InterfazDibujo:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujo")
        self.root.geometry("420x380")
        self.root.resizable(0, 0)
        self.root.config(padx=20, pady=20)

        # =============================
        # VARIABLES
        # =============================
        self.var_valor = tk.StringVar()
        self.var_tipo_Dibujo = tk.StringVar()
        self.var_fecha_Realizacion = tk.StringVar()
        self.var_Autor = tk.StringVar()

        self.err_valor = tk.StringVar()
        self.err_tipo_Dibujo = tk.StringVar()
        self.err_fecha_Realizacion = tk.StringVar()
        self.err_Autor = tk.StringVar()

        self.validador = Validaciones()

        # Crear la interfaz
        self.crear_interfaz()

        # Cerrar ventana con confirmación
        self.root.protocol("WM_DELETE_WINDOW", self.el_usuario_quiere_salir)

    # =============================
    # FUNCIONES
    # =============================
    def el_usuario_quiere_salir(self):
        if askyesno("Salir de la aplicación", "¿Estás seguro de que quieres cerrar la aplicación?"):
            self.root.destroy()

    def limpiar_campos_texto(self):
        """Limpia todos los campos y mensajes de error."""
        for var, err in [
            (self.var_valor, self.err_valor),
            (self.var_tipo_Dibujo, self.err_tipo_Dibujo),
            (self.var_fecha_Realizacion, self.err_fecha_Realizacion),
            (self.var_Autor, self.err_Autor)
        ]:
            var.set("")
            err.set("")

        # Restaurar color de fondo
        self.entry_valor.config(bg="white")
        self.entry_tipo_Dibujo.config(bg="white")
        self.entry_fecha_Realizacion.config(bg="white")
        self.entry_Autor.config(bg="white")

    def enviar(self):
        """Valida y guarda los datos del formulario."""
        entradas = {
            "valor": self.entry_valor,
            "tipo_dibujo": self.entry_tipo_Dibujo,
            "fecha_realizacion": self.entry_fecha_Realizacion,
            "autor": self.entry_Autor
        }

        ok = self.validador.validar_campos(entradas)

        # Validar campos obligatorios
        obligatorios = [
            (self.var_valor.get().strip() != "", self.err_valor, "El valor es obligatorio."),
            (self.var_tipo_Dibujo.get().strip() != "", self.err_tipo_Dibujo, "El tipo de dibujo es obligatorio."),
            (self.var_fecha_Realizacion.get().strip() != "", self.err_fecha_Realizacion, "La fecha de realización es obligatoria."),
            (self.var_Autor.get().strip() != "", self.err_Autor, "El autor es obligatorio."),
        ]

        for lleno, err_var, msg in obligatorios:
            if not lleno and err_var.get() == "":
                err_var.set(msg)
                ok = False

        if not ok:
            showerror("Errores de validación", "Por favor complete los campos marcados en rojo.")
            return

        showinfo("OK", "Formulario válido. ¡Datos guardados!")

    # =============================
    # CREAR INTERFAZ
    # =============================
    def crear_interfaz(self):
        label_opts = dict(sticky="e", padx=(0,10), pady=(0,8))
        entry_opts = dict(sticky="w", padx=(0,10), pady=(0,8))

        # Valor
        tk.Label(self.root, text="Valor").grid(row=0, column=0, **label_opts)
        self.entry_valor = tk.Entry(self.root, textvariable=self.var_valor, width=25)
        self.entry_valor.grid(row=0, column=1, **entry_opts)
        tk.Label(self.root, textvariable=self.err_valor, fg="#d83c8a").grid(row=1, column=1, sticky="w", pady=(0,8))

        # Tipo Dibujo
        tk.Label(self.root, text="Tipo Dibujo").grid(row=2, column=0, **label_opts)
        self.entry_tipo_Dibujo = tk.Entry(self.root, textvariable=self.var_tipo_Dibujo, width=25)
        self.entry_tipo_Dibujo.grid(row=2, column=1, **entry_opts)
        tk.Label(self.root, textvariable=self.err_tipo_Dibujo, fg="#d83c8a").grid(row=3, column=1, sticky="w", pady=(0,8))

        # Fecha de Realización
        tk.Label(self.root, text="Fecha de Realización").grid(row=4, column=0, **label_opts)
        self.entry_fecha_Realizacion = tk.Entry(self.root, textvariable=self.var_fecha_Realizacion, width=25)
        self.entry_fecha_Realizacion.grid(row=4, column=1, **entry_opts)
        tk.Label(self.root, textvariable=self.err_fecha_Realizacion, fg="#d83c8a").grid(row=5, column=1, sticky="w", pady=(0,8))

        # Autor
        tk.Label(self.root, text="Autor").grid(row=6, column=0, **label_opts)
        self.entry_Autor = tk.Entry(self.root, textvariable=self.var_Autor, width=25)
        self.entry_Autor.grid(row=6, column=1, **entry_opts)
        tk.Label(self.root, textvariable=self.err_Autor, fg="#d83c8a").grid(row=7, column=1, sticky="w", pady=(0,8))

        # Botones
        boton_frame = tk.Frame(self.root)
        boton_frame.grid(row=8, column=0, columnspan=2, pady=(18,0))
        tk.Button(boton_frame, text="Validar Información", command=self.enviar, width=18).pack(side="left", padx=10)
        tk.Button(boton_frame, text="Limpiar", command=self.limpiar_campos_texto, width=12).pack(side="left", padx=10)

        # Validación en tiempo real
        self.entry_valor.bind("<KeyRelease>", lambda e: self.validador.validar_valor(self.entry_valor))
        self.entry_tipo_Dibujo.bind("<KeyRelease>", lambda e: self.validador.validar_tipo_dibujo(self.entry_tipo_Dibujo))
        self.entry_fecha_Realizacion.bind("<KeyRelease>", lambda e: self.validador.validar_fecha_realizacion(self.entry_fecha_Realizacion))
        self.entry_Autor.bind("<KeyRelease>", lambda e: self.validador.validar_autor(self.entry_Autor))
