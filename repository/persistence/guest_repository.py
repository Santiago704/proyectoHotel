from domain.models.guest import guest

class guest_repository:
    def __init__(self, conexion):
        self.conexion = conexion

    def save(self, guest):
        query = ("INSERT INTO guest (name, last_name, id, occupation, phone, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        params = (
            guest.name,
            guest.last_name,
            guest.id,
            guest.occupation,
            guest.phone,
            guest.email,
            guest.password,
        )

        self.conexion.execute_query(query, params)