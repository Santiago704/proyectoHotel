#Importar de service, optService, bedroom y guest
from domain.models.service import service
from domain.models.guest import guest
from domain.models.bedroom import bedroom

class booking(service, guest, bedroom):

    def __init__(self, checkin, checkout, booking_id,  service_name, price, id, name , last_name, phone, email, password, status, origin, occupation ):
        service.__init__(self, service_name, price)
        guest.__init__(self, id, name, last_name, phone, email, password, status, origin, occupation)

        self._checkin = checkin
        self._checkout = checkout
        self._booking_id = booking_id

    @property
    def checkin(self):
        return self._checkin

    @checkin.setter
    def checkin(self, checkin):
        self._checkin = checkin

    @property
    def checkout(self):
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        self._checkout = checkout

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id):
        self._booking_id = booking_id