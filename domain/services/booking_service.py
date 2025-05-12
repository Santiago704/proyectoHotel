from datetime import datetime
from domain.exceptions.booking_exceptions import bookingInvalidException
from domain.models.booking import Booking

class Booking_service:
    def __init__(self, repository):
        self.repository = repository

    def allow_booking(self, checkin_string, checkout_string, room_id, guest_id=1, service_id=1):
        checkin = datetime.strptime(checkin_string, "%d-%m-%Y").date()
        checkout = datetime.strptime(checkout_string, "%d-%m-%Y").date()

        # Validaciones
        if checkin >= checkout:
            raise bookingInvalidException("La fecha de check-in debe ser anterior a la de check-out")

        if checkin < datetime.now().date():
            raise bookingInvalidException("La fecha de check-in debe estar en el futuro")

        # Crear una nueva reserva
        new_booking = Booking(
            booking_id=None,
            guest_id=guest_id,
            bedroom_id=int(room_id),
            service_id=service_id,
            checkin=checkin,
            checkout=checkout
        )

        self.repository.save(new_booking)
        return True