class service :
    def __init__(self, service_name, price):
        self.service_name= service_name
        self._price = price


    # service_id
    @property
    def service_name(self):
        return self.service_name

    @service_name.setter
    def service_name(self, service_name):
        self.service_name = service_name


    # price
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self,price):
        self.price = price

