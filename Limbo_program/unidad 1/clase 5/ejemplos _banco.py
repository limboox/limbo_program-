import flet as ft
import threading
import time
def main(page: ft.Page):
    def __init__(self) -> None:
        self.saldo = 0
        self.candado = threading.Lock()  # crear un candado (lock)

    def depositar(self, monto, nombre_cliente):
        self.candado.acquire()  # inicio de sección crítica
        print("%s depositando monto: %d , Saldo actual: %d" % (nombre_cliente, monto, self.saldo))
        time.sleep(10/1000)
        self.saldo = self.saldo + monto
        print("%s verificando saldo: ahora es %d" % (nombre_cliente, self.saldo))
        self.candado.release()  # fin de sección crítica
        
    def __init__(self, nombre_cliente: str, cuenta: CuentaBancaria):
        super(HiloCliente, self).__init__()
        self.nombre_cliente = nombre_cliente
        self.cuenta = cuenta
    
    def run(self) -> None:
        self.cuenta.depositar(1000, self.nombre_cliente)
        return super().run()

# Programa principal
cuenta = CuentaBancaria()
cliente1 = HiloCliente("Smith", cuenta)
cliente2 = HiloCliente("Steves", cuenta)

cliente1.start()
cliente2.start()
ft.app(target=main)