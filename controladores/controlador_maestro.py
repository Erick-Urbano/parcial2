from controladores.observer import Observador

class ControlMaestro(Observador):
    _instancia = None  # patrón Singleton

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        self.alertas = []

    def actualizar(self, nombre_subsistema, mensaje):
        alerta = f"[{nombre_subsistema}] {mensaje}"
        self.alertas.append(alerta)
        print(f"🚨 {alerta}")

    def mostrar_alertas(self):
        print("\n=== ALERTAS DEL SISTEMA ===")
        for a in self.alertas:
            print(a)
        print("===========================\n")
