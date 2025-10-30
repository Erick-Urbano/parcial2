from modelos.subsistema import Subsistema

class SistemaTemperatura(Subsistema):
    def __init__(self):
        super().__init__("Control de Temperatura")
        self.temperatura = 22
        self.min_temp = 18
        self.max_temp = 28

    def subir(self):
        self.temperatura += 1
        print(f"🌡️ Temperatura actual: {self.temperatura}")
        if self.temperatura > self.max_temp:
            self.notificar("Temperatura demasiado alta.")

    def bajar(self):
        self.temperatura -= 1
        print(f"🌡️ Temperatura actual: {self.temperatura}")
        if self.temperatura < self.min_temp:
            self.notificar("Temperatura demasiado baja.")
