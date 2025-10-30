from modelos.subsistema import Subsistema

class SistemaLuces(Subsistema):
    def __init__(self):
        super().__init__("Control de Luces")
        self.habitaciones = {"Sala": True, "Cocina": False}

    def encender(self, habitacion):
        self.habitaciones[habitacion] = True
        print(f"{habitacion} encendida.")

    def apagar(self, habitacion):
        self.habitaciones[habitacion] = False
        print(f"{habitacion} apagada.")

    def verificar_luces(self):
        if not any(self.habitaciones.values()):
            self.notificar("Todas las luces están apagadas.")
