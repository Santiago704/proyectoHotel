class Booking:
    def __init__(self, booking_id, guest_id, bedroom_id, service_id, checkin, checkout):
        self._booking_id = booking_id
        self._guest_id = guest_id
        self._bedroom_id = bedroom_id
        self._service_id = service_id
        self._checkin = checkin
        self._checkout = checkout

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id):
        self._booking_id = booking_id

    @property
    def guest_id(self):
        return self._guest_id

    @guest_id.setter
    def guest_id(self, guest_id):
        self._guest_id = guest_id

    @property
    def bedroom_id(self):
        return self._bedroom_id

    @bedroom_id.setter
    def bedroom_id(self, bedroom_id):
        self._bedroom_id = bedroom_id

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id

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