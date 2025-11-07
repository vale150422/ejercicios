import re
from tkinter import Entry

class Validaciones:
    def __init__(self):
        pass

    # ------------------------------
    # Validaciones de texto y números
    # ------------------------------
    def validar_valor(self, entry: Entry) -> bool:
        """Valida que el valor sea un número de hasta 5 dígitos."""
        txt = entry.get()
        patron = r"^\d{1,5}$"
        if re.match(patron, txt):
            entry.config(bg="white")
            return True
        else:
            entry.config(bg="red")
            return False

    def validar_tipo_dibujo(self, entry: Entry) -> bool:
        """Valida que el tipo de dibujo contenga solo letras y espacios."""
        txt = entry.get()
        patron = r"^[A-Za-z\s]+$"
        if re.match(patron, txt):
            entry.config(bg="white")
            return True
        else:
            entry.config(bg="red")
            return False

    def validar_fecha_realizacion(self, entry: Entry) -> bool:
        txt = entry.get()
        # Permite hasta 10 caracteres y solo números y guiones
        patron_parcial = r"^[\d-]{0,10}$"
        patron_completo = r"^\d{4}-\d{2}-\d{2}$"
        
        if re.match(patron_parcial, txt):
            if re.match(patron_completo, txt):
                entry.config(bg="white")  # Fecha completa y correcta
            else:
                entry.config(bg="yellow")  # Fecha incompleta pero formato posible
            return True
        else:
            entry.config(bg="red")  # Carácter inválido
            return False


    def validar_autor(self, entry: Entry) -> bool:
        """Valida que el autor contenga solo letras y espacios."""
        txt = entry.get()
        patron = r"^[A-Za-z\s]+$"
        if re.match(patron, txt):
            entry.config(bg="white")
            return True
        else:
            entry.config(bg="red")
            return False

    # ------------------------------
    # Validación general
    # ------------------------------
    def validar_campos(self, entradas: dict) -> bool:
        """
        Recibe un diccionario con las entradas del formulario:
        {
            "valor": entry_valor,
            "tipo_dibujo": entry_tipo,
            "fecha_realizacion": entry_fecha,
            "autor": entry_autor
        }
        Retorna True si todo es válido.
        """
        ok = True
        ok &= self.validar_valor(entradas["valor"])
        ok &= self.validar_tipo_dibujo(entradas["tipo_dibujo"])
        ok &= self.validar_fecha_realizacion(entradas["fecha_realizacion"])
        ok &= self.validar_autor(entradas["autor"])
        return ok
