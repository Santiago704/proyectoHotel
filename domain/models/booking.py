
class booking():

    def __init__(self, checkin, checkout):
        self._checkin = checkin
        self._checkout = checkout

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