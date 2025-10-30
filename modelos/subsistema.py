class Subsistema:
    def __init__(self, nombre):
        self.nombre = nombre
        self.baterias = [100, 80, 70]
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self, mensaje):
        for obs in self.observadores:
            obs.actualizar(self.nombre, mensaje)

    def verificar_baterias(self):
        if all(b < 100 for b in self.baterias):
            self.notificar("Alerta: ninguna batería está al 100%.")
