import re
from domain.models.guest import guest
from domain.exceptions.guest_exceptions import guestInvalidException

class guest_service:
    def __init__(self, repository):
        self.repository = repository

    def register_guest(self,id, name , last_name, phone, email, password, status, origin, occupation):
        if not id or not name or not last_name or not phone or not email or not password or not status or not origin or not occupation:
            raise guestInvalidException("Todos los datos son obligatorio")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$',email):
            raise guestInvalidException("mail no valido ")
        guest_saved = guest(id, name , last_name, phone, email, password, status, origin, occupation)
        self.repository.save(guest_saved)
        return guest_saved

    def login_guest(self, email, password):
        result = self.repository.login(email, password)
        if result:
            print("login exitoso")
            return result
        else:
            raise ValueError("correo o contraseña incorrectos")