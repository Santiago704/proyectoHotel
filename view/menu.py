from domain.models.guest import guest
from domain.services.guest_service import guest_service
from application.guest_input import guest_input
from repository.conexion.bd_connection import Conexion
from repository.persistence.guest_repository import guest_repository


class menu_app:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='proyectohotelbd')
        self.db.connection()
        self.repository = guest_repository(self.db)
        self.guest_service = guest_service(self.repository)
        self.guest_input = guest_input()

    def init_app(self):
        while True:
            try:
                init = int(input("Presione 1 para inicializar: "))
                if init != 1:
                    print('Para empezar solo es válida la opción 1.')
                    continue
                break
            except ValueError:
                print("Opción inválida, digite un número")

        while True:
            try:
                option = int(input("1. Login  2. Registro  3. Salir: "))

                match option:
                    case 1:
                        try:
                            if self.guest_input.login(self.guest_service):
                                self.principal_menu()
                            continue
                        except ValueError:
                            print("Error en el login")
                            continue
                    case 2:
                        try:
                            self.guest_input.register(self.guest_service)
                            continue
                        except ValueError:
                            print("Error en el registro")
                            continue
                    case 3:
                        print("Salió del sistema")
                        break
                    case _:
                        print("Digite una opción válida.")
            except ValueError:
                print("Opción inválida, digite un número.")

    def principal_menu(self):
        while True:
            try:
                option = int(input("1. Consultar habitaciones  2. Reservar  3. Salir: "))
                match option:
                    case 1:
                        #lógica para consultar habitaciones
                        break
                    case 2:
                        #lógica para reservar una habitación
                        break
                    case 3:
                        print("Saliendo al menú principal.")
                        break
                    case _:
                        print("Digite una opción válida")
            except ValueError:
                print(" digite un número")