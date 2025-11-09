import threading
import queue
import time

class GeneradorTareas(threading.Thread):
    def __init__(self, q, n, consumidores):
        super().__init__()
        self.q = q
        self.n = n
        self.consumidores = consumidores

    def run(self):
        # Poner los números 1..n en la cola con pequeñas pausas
        for i in range(1, self.n + 1):
            print(f"Generando tarea: {i}")
            self.q.put(i)
            time.sleep(0.2)

        # Enviar un centinela None por cada consumidor
        for _ in range(self.consumidores):
            self.q.put(None)


class Trabajador(threading.Thread):
    def __init__(self, q, nombre):
        super().__init__()
        self.q = q
        self.nombre = nombre

    def run(self):
        while True:
            # Obtener un ítem de la cola
            item = self.q.get()

            # Si es None, terminar
            if item is None:
                print(f"{self.nombre} finalizando.")
                self.q.task_done()
                break

            # Procesar el ítem (por ejemplo, calcular su cuadrado)
            resultado = item * item
            print(f"{self.nombre} procesó {item} -> {resultado}")

            # Marcar tarea como hecha
            self.q.task_done()
            time.sleep(0.3)


def main():
    # Crear cola
    q = queue.Queue()

    # Crear consumidores (trabajadores)
    consumidores = 2
    trabajadores = [Trabajador(q, f"Trabajador-{i+1}") for i in range(consumidores)]

    # Crear productor (generador de tareas)
    generador = GeneradorTareas(q, 10, consumidores)

    # Iniciar hilos
    generador.start()
    for t in trabajadores:
        t.start()

    # Esperar a que todas las tareas se completen
    q.join()

    # Esperar a que los hilos terminen
    generador.join()
    for t in trabajadores:
        t.join()

    print("Todas las tareas han sido procesadas.")


if __name__ == "__main__":
    main()
