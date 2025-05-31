from domain.services.guest_service import guest_service

class guest_input:
    def __init__(self):
        pass

    def register(self, guest_service):
        try:
            id = input("Ingrese su documento de identidad: ")
            name = input("Ingrese su nombre: ")
            last_name = input("Ingrese su apellido: ")
            phone = input("Ingrese su teléfono: ")
            email = input("Ingrese su correo: ")
            password = input("Ingrese su contraseña: ")
            status = input("Seleccione el estado: ")
            origin = input("Ingrese su ciudad de origen: ")
            occupation = input("Ingrese su ocupación: ")

            #guest_service.register_guest(
            #    id, name, last_name, phone, email, password, status, origin, occupation
            #)
            ##Le quite name
            guest_service.register_guest(
                id, name, last_name, phone, email, password, status, origin, occupation
            )
            print("Registro guardado exitosamente")

        except Exception as e:
            print("Error en el registro:", e)

    def login(self, guest_service):
        try:
            email = input("Ingrese el correo: ")
            password = input("Ingrease la contraseña: ")

            guest = guest_service.login_guest(email, password)
            return True

        except Exception as e:
            print("Error en el login:", e)
            return False