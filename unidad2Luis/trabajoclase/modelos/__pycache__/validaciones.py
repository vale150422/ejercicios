import re

class validaciones():
    def __init__(self):
        pass

    def validar_letras(valor):
        patron = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$")
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True