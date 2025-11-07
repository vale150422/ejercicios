import requests

class Comunicacion:
    def __init__(self):
        # URL base de tu API Django (ajusta si el puerto es distinto)
        self.url = 'http://127.0.0.1:8000/v1/clase/'

    def guardar(self, marca, talla, valor, fecha_fabricacion):
        """
        Envía los datos del formulario al backend Django para crear una nueva 'Clase'.
        """
        try:
            # Arma el cuerpo del JSON que se enviará al backend
            data = {
                "tema": marca,
                "descripcion": f"Talla: {talla}, Valor: {valor}, Fecha: {fecha_fabricacion}",
                "numero_clase": 1  # Puedes cambiarlo o hacerlo dinámico si quieres
            }

            print("📤 Enviando datos al backend:", data)
            response = requests.post(self.url, json=data)

            print("📥 Respuesta del servidor:", response.status_code, response.text)

            if response.status_code == 201:
                return True
            else:
                print("⚠️ Error al guardar:", response.text)
                return False

        except requests.exceptions.ConnectionError:
            print("❌ Error: No se pudo conectar al servidor Django. ¿Está corriendo en el puerto 8000?")
            return False
        except Exception as e:
            print("⚠️ Excepción en guardar():", e)
            return False

    def consultar_todo(self):
        """
        Obtiene todas las clases registradas desde el backend.
        """
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.json()
            else:
                print("⚠️ Error al consultar:", response.text)
                return []
        except Exception as e:
            print("❌ Error de conexión:", e)
            return []
