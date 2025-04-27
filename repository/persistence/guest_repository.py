from domain.models.guest import guest

class guest_repository:
    def __init__(self, conexion):
        self.conexion = conexion

    def save(self, guest):
        # Primero insertamos en la tabla users
        query_users = ("INSERT INTO users (name, last_name, id, phone, email, password) VALUES (%s, %s, %s, %s, %s, %s)")
        params_users = (
            guest.name,
            guest.last_name,
            guest.id,  # El id que se pasa es el mismo para ambas tablas
            guest.phone,
            guest.email,
            guest.password
        )
        self.conexion.execute_query(query_users, params_users)

        # Luego insertamos en la tabla guest usando el mismo id
        query_guest = ("INSERT INTO guest (id, occupation) VALUES (%s, %s)")
        params_guest = (
            guest.id,  # Usamos el mismo id
            guest.occupation
        )
        self.conexion.execute_query(query_guest, params_guest)