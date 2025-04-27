from domain.services.guest_service import guest_service
from domain.models.guest import guest
from repository.persistence.guest_repository import guest_repository

class guest_input:
    def __init__(self, conexion):
        self.guest = guest(None, None, None, None, None, None, None, None, None)
        self.guest_repository = guest_repository(conexion)

    def register(self, guest, db):
        id = int(input("Ingrese su documento de identidad: "))
        self.guest.id = id
        name = input("Ingrese su nombre: ")
        self.guest.name = name
        last_name = input("Ingrese su apellido: ")
        self.guest.last_name = last_name
        phone = input("Ingrese su teléfono: ")
        self.guest.phone = phone
        email = input("Ingrese su correo: ")
        self.guest.email = email
        password = input("Ingrese su contraseña: ")
        self.guest.password = password
        status = input("Seleccione el estado: ")
        self.guest.status = status
        origin = input("Ingrese su ciudad de origen: ")
        self.guest.origin = origin
        occupation = input("Ingrese su ocupacion: ")
        self.guest.occupation = occupation

        self.guest_repository.save(self.guest)