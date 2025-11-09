import threading
import time

def tarea(nombre, duracion):
    # Imprimir el inicio de la tarea
    print(f"Iniciando tarea {nombre} (duración: {duracion}s)")
    # Dormir la duración indicada
    time.sleep(duracion)
    # Imprimir el final de la tarea
    print(f"Finalizando tarea {nombre}")

def main():
    # Crear tres hilos con distintas duraciones
    hilo1 = threading.Thread(target=tarea, args=("A", 1.2))
    hilo2 = threading.Thread(target=tarea, args=("B", 0.8))
    hilo3 = threading.Thread(target=tarea, args=("C", 1.5))

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()
    hilo3.start()

    # Esperar a que todos terminen
    hilo1.join()
    hilo2.join()
    hilo3.join()

    # Imprimir mensaje final
    print("Terminado")

if __name__ == "__main__":
    main()
