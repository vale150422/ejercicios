import threading
import time

class LoggerDaemon(threading.Thread):
    def __init__(self, intervalo):
        super().__init__(daemon=True)
        self.intervalo = intervalo

    def run(self):
        # Imprimir un mensaje periódico de log mientras el programa corre
        while True:
            print("[LoggerDaemon] Programa en ejecución...")
            time.sleep(self.intervalo)


class TrabajoPesado(threading.Thread):
    def __init__(self, pasos):
        super().__init__()
        self.pasos = pasos

    def run(self):
        # Simular pasos con prints y sleeps
        for i in range(1, self.pasos + 1):
            print(f"Ejecutando paso {i}/{self.pasos}")
            time.sleep(1)
        print("Trabajo pesado completado.")


def main():
    # Crear el logger y el trabajador
    logger = LoggerDaemon(2)
    trabajador = TrabajoPesado(5)

    # Iniciar ambos hilos
    logger.start()
    trabajador.start()

    # Unir el trabajador (el logger daemon se detendrá al cerrar el programa)
    trabajador.join()

    # Imprimir mensaje final
    print("Programa finalizado.")


if __name__ == "__main__":
    main()
