
class bedroom_repository:
    def __int__(self, conexion):
        self.conexion = conexion

    def save(self, bedroom):
        query = ("INSERT INTO bedroom (room_id, category, price, available) VALUES (%, %, %,%)")
        params = (
           bedroom.room_id,
           bedroom.category,
           bedroom.price,
           bedroom.available
        )

        self.conexion.execute_query(query, params)
