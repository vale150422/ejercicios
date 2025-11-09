import threading
import random
import time

class Cuenta:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def depositar(self, monto):
        # Proteger con lock
        with self.lock:
            saldo_actual = self.saldo
            saldo_actual += monto
            time.sleep(0.01)  # Simular tiempo de operación
            self.saldo = saldo_actual
            print(f"Depósito de {monto} | Saldo actual: {self.saldo}")

    def retirar(self, monto):
        # Proteger con lock
        with self.lock:
            if self.saldo >= monto:
                saldo_actual = self.saldo
                saldo_actual -= monto
                time.sleep(0.01)  # Simular tiempo de operación
                self.saldo = saldo_actual
                print(f"Retiro de {monto} | Saldo actual: {self.saldo}")
            else:
                print(f"Fondos insuficientes para retirar {monto} | Saldo: {self.saldo}")


class OperadorCuenta(threading.Thread):
    def __init__(self, cuenta, operaciones):
        super().__init__()
        self.cuenta = cuenta
        self.operaciones = operaciones

    def run(self):
        for _ in range(self.operaciones):
            # Elegir aleatoriamente entre depositar o retirar
            monto = random.randint(10, 100)
            if random.choice([True, False]):
                self.cuenta.depositar(monto)
            else:
                self.cuenta.retirar(monto)
            time.sleep(0.05)


def main():
    # Crear la cuenta con saldo inicial
    cuenta = Cuenta(1000)

    # Crear varios hilos que operan sobre la misma cuenta
    hilos = [OperadorCuenta(cuenta, 5) for _ in range(3)]

    # Iniciar los hilos
    for h in hilos:
        h.start()

    # Esperar a que terminen
    for h in hilos:
        h.join()

    # Mostrar saldo final
    print(f"Saldo final: {cuenta.saldo}")


if __name__ == "__main__":
    main()
