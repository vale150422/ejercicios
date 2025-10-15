import tkinter as tk 
from controladores.validaciones import validaciones
from modelos.almacen import almacen 


class interfaz():
    def mostrar_interfaz():
        ventanaPrincipal = tk.Tk()

        almacen = almacen(ventanaPrincipal)


    ventana = tk.Tk()
    ventana.title("Prendas de Vestir")
    ventana.geometry("400x550")


    def validar_marca(*args):
        texto = marca.get()
        if texto and not texto.isalpha():
            lbl_error_marca.config(text="Solo se pueden escribir letras", fg="red")
        elif not texto:
            lbl_error_marca.config(text="Campo obligatorio", fg="red")
        else:
            lbl_error_marca.config(text="")

    def validar_talla(*args):
        texto = talla.get()
        if texto and not texto.isdigit():
            lbl_error_talla.config(text="Solo se pueden escribir números", fg="red")
        elif not texto:
            lbl_error_talla.config(text="Campo obligatorio", fg="red")
        else:
            lbl_error_talla.config(text="")

    def validar_valor(*args):
        texto = valor.get()

        if texto and not(r"\d+(\.\d+)?", texto):
            lbl_error_valor.config(text="Solo números (puede usar .)", fg="red")
        elif not texto:
            lbl_error_valor.config(text="Campo obligatorio", fg="red")
        else:
            lbl_error_valor.config(text="")

    def validar_fecha(*args):
        texto = fecha.get()

        if texto and not (r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}", texto):
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



    titulo = tk.Label(ventana, text="Tema: Prenda de vestir", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    frame_campos = tk.Frame(ventana)
    frame_campos.pack(pady=5)


    tk.Label(frame_campos, text="Marca", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
    marca = tk.StringVar()
    marca.trace_add("write", validar_marca)
    entry_marca = tk.Entry(frame_campos, textvariable=almacen.marca, width=25)
    entry_marca.pack(padx=10, pady=2)
    lbl_error_marca = tk.Label(frame_campos, text="", fg="red")
    lbl_error_marca.pack(anchor="w", padx=10)


    tk.Label(frame_campos, text="Talla", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
    talla = tk.StringVar()
    talla.trace_add("write", validar_talla)
    entry_talla = tk.Entry(frame_campos, textvariable=almacen.talla, width=25)
    entry_talla.pack(padx=10, pady=2)
    lbl_error_talla = tk.Label(frame_campos, text="", fg="red")
    lbl_error_talla.pack(anchor="w", padx=10)


    tk.Label(frame_campos, text="Valor", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
    valor = tk.StringVar()
    valor.trace_add("write", validar_valor)
    entry_valor = tk.Entry(frame_campos, textvariable=almacen.valor, width=25)
    entry_valor.pack(padx=10, pady=2)
    lbl_error_valor = tk.Label(frame_campos, text="", fg="red")
    lbl_error_valor.pack(anchor="w", padx=10)


    tk.Label(frame_campos, text="Fecha de Fabricación", font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
    fecha = tk.StringVar()
    fecha.trace_add("write", validar_fecha)
    entry_fecha = tk.Entry(frame_campos, textvariable=almacen.fecha, width=25)
    entry_fecha.pack(padx=10, pady=2)
    lbl_error_fecha = tk.Label(frame_campos, text="", fg="red")
    lbl_error_fecha.pack(anchor="w", padx=10)

    boton_guardar = tk.Button(
        ventana, text="Guardar", font=("Arial", 12, "bold"),
        bg="green", fg="white", command=validar_guardar
    )
    boton_guardar.pack(pady=20)

    ventana.mainloop()