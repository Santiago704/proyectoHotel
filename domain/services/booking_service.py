from datetime import datetime
from domain.exceptions.booking_exceptions import bookingInvalidException
from domain.models.booking import booking

class booking_service:
    def __init__(self, repository):
        self.repository = repository

    def allow_booking(self, checkin, checkout):
        if checkin >= checkout:
            raise bookingInvalidException("la fecha de checkin debe ser anterior")

        if checkin < datetime.now():
            raise bookingInvalidException("la fecha de checkin debe estar en futuro")

        self.repository.save(booking)
        return True