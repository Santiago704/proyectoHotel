from domain.models.guest import guest

class guest_repository:
    def __init__(self, conexion):
        self.conexion = conexion

    def save(self, guest):
        query_users = ("INSERT INTO users (name, last_name, id, phone, email, password) VALUES (%s, %s, %s, %s, %s, %s)")
        params_users = (
            guest.name,
            guest.last_name,
            guest.id,
            guest.phone,
            guest.email,
            guest.password
        )
        self.conexion.execute_query(query_users, params_users)

        query_guest = ("INSERT INTO guest (id, occupation) VALUES (%s, %s)")
        params_guest = (
            guest.id,
            guest.occupation
        )
        self.conexion.execute_query(query_guest, params_guest)

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.conexion.fetch_one(query, params)
        return result
