class optservice :
    def __init__(self, optservice_name, price):
        self._optservice_name= optservice_name
        self._price = price


    @property
    def optservice_name (self):
        return self._optservice_name

    @optservice_name.setter
    def optservice_name(self,optservice_name):
        self._optservice_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price

