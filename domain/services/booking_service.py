from domain.models.booking import booking

class booking_service:
    def __init__(self, repository):
        self.repository = repository

    def allow_booking(self, id, name):
