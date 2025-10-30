from modelos.subsistema import Subsistema

class SistemaAcceso(Subsistema):
    def __init__(self):
        super().__init__("Control de Acceso")
        self.intentos_fallidos = 0
        self.usuarios = {"admin": "1234"}

    def ingresar(self, usuario, contraseña):
        if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
            print("Acceso permitido.")
            self.intentos_fallidos = 0
        else:
            self.intentos_fallidos += 1
            print("Acceso denegado.")
            if self.intentos_fallidos >= 3:
                self.notificar("¡Alarma! Demasiados intentos fallidos.")
