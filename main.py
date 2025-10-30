from modelos.luces import SistemaLuces
from modelos.temperatura import SistemaTemperatura
from modelos.residuos import SistemaResiduos
from modelos.acceso import SistemaAcceso
from controladores.controlador_maestro import ControlMaestro
from vistas.vista_consola import VistaConsola

def main():
    # Crear instancias
    maestro = ControlMaestro()
    luces = SistemaLuces()
    temp = SistemaTemperatura()
    residuos = SistemaResiduos()
    acceso = SistemaAcceso()

    # Conectar subsistemas al observador
    for s in [luces, temp, residuos, acceso]:
        s.agregar_observador(maestro)

    while True:
        VistaConsola.mostrar_menu()
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            luces.encender("Sala")
        elif opcion == "2":
            luces.apagar("Sala")
        elif opcion == "3":
            temp.subir()
        elif opcion == "4":
            temp.bajar()
        elif opcion == "5":
            residuos.agregar_residuo(3)
        elif opcion == "6":
            u = input("Usuario: ")
            c = input("Contraseña: ")
            acceso.ingresar(u, c)
        elif opcion == "7":
            maestro.mostrar_alertas()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
