from domain.models.guest import guest
from domain.services.guest_service import guest_service
from application.guest_input import guest_input
from repository.conexion.bd_connection import Conexion


class menu_app:

    db = Conexion(host='localhost', port=3306, user='root', password="", database='proyectohotelbd')
    db.connection()

    def __init__(self):
        self.guest = guest(None, None,None,None,None,None,None,None,None)
        self.guest_service = guest_service(self.db)
        self.guest_input = guest_input(self.db)


    def init_app(self):
        init = (int(input("Presione 1 para inicializar")))

        while init != 0:

            option = int(input("1. Login 2. registro 3. salir"))

            if option == 1:
                print("Login")
            elif option == 2:
                print("Registro")
                self.guest_input.register(self.guest,self.db)