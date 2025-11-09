import threading
import time

class Temporizador(threading.Thread):
    def __init__(self, limite, reset_event, stop_event):
        super().__init__()
        self.limite = limite
        self.reset_event = reset_event
        self.stop_event = stop_event

    def run(self):
        contador = 0
        while not self.stop_event.is_set():
            print(f"Tiempo: {contador}s")
            time.sleep(1)
            contador += 1

            # Si se presiona Enter, se reinicia el temporizador
            if self.reset_event.is_set():
                print("Reiniciando temporizador...")
                contador = 0
                self.reset_event.clear()

            # Si llega al límite, se detiene
            if contador >= self.limite:
                print("¡Tiempo completado!")
                self.stop_event.set()


class EscuchaReset(threading.Thread):
    def __init__(self, reset_event):
        super().__init__(daemon=True)
        self.reset_event = reset_event

    def run(self):
        while True:
            input()  # Espera que el usuario presione Enter
            self.reset_event.set()


def main():
    # Crear eventos
    reset_event = threading.Event()
    stop_event = threading.Event()

    # Crear hilos
    temporizador = Temporizador(10, reset_event, stop_event)
    escucha = EscuchaReset(reset_event)

    # Iniciar hilos
    temporizador.start()
    escucha.start()

    # Esperar a que el temporizador termine
    temporizador.join()

    print("Programa terminado.")


if __name__ == "__main__":
    main()

