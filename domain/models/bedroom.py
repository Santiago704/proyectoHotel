
class bedroom:
    def __init__(self, room_id, category, price, available = True):
        self.room_id = room_id
        self.catagory = category
        self.price = price
        self.available = available

    # room_id
    @property
    def room_id(self):
        return self.room_id

    @room_id.setter
    def room_id(self, room_id):
        self.room_id = room_id

    # category
    @property
    def category(self):
        return self.catagory

    @category.setter
    def category(self, category):
        self.category = category

    # price
    @property
    def price(self):
        return self.price

    @category.setter
    def category(self, price):
        self.price = price

    # avaible
    @property
    def avaible(self):
        return self.available

    @category.setter
    def avaible(self, avaible):
        self.available = avaible