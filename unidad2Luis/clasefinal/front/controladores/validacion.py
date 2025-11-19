import re

class Validaciones():

    def __init__(Self):
        pass

    def validar_letras(valor):
        patron = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$")
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True
    
    def validar_numeros(valor):
        patron_n = re.compile(r"^\d+$")
        resultado_n = patron_n.match(valor.get()) is not None
        if not resultado_n:
            return False
        return True
    
    def validar_letrasynumeros(valor):
        patron_nn = re.compile(r"^[A-Za-z0-9]+$")
        resultado_nn = patron_nn.match(valor.get()) is not None
        if not resultado_nn:
            return False
        return True
