# controladores/comunicacion.py
class Comunicacion:
    def __init__(self):
        self.data = []
        self.auto_id = 1

    def guardar(self, marca, talla, valor, fecha):
        """
        Guarda cada campo por separado en un registro.
        """
        registro = {
            "id": self.auto_id,
            "marca": marca,
            "talla": talla,
            "valor": valor,
            "fecha": fecha
        }
        self.data.append(registro)
        self.auto_id += 1
        return True

    def consultar(self, id_):
        try:
            id_int = int(id_)
        except:
            return {"error": "ID inválido"}

        for r in self.data:
            if r["id"] == id_int:
                return r
        return {"error": "No encontrado"}

    def consultar_todo(self):
        # devolver copia para seguridad
        return list(self.data)

    def eliminar(self, id_):
        try:
            id_int = int(id_)
        except:
            return False
        before = len(self.data)
        self.data = [r for r in self.data if r["id"] != id_int]
        return len(self.data) < before

    def actualizar(self, id_, marca, talla, valor, fecha):
        try:
            id_int = int(id_)
        except:
            return None
        for r in self.data:
            if r["id"] == id_int:
                r["marca"] = marca
                r["talla"] = talla
                r["valor"] = valor
                r["fecha"] = fecha
                return r
        return None
