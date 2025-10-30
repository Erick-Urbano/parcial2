from modelos.subsistema import Subsistema

class SistemaResiduos(Subsistema):
    def __init__(self):
        super().__init__("Control de Residuos")
        self.residuos = 5
        self.limite = 10

    def agregar_residuo(self, cantidad):
        self.residuos += cantidad
        print(f"🗑️ Residuos actuales: {self.residuos}")
        if self.residuos > self.limite:
            self.notificar("Alerta: exceso de residuos sin evacuar.")
