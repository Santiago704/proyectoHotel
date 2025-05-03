from domain.models.booking import booking

class booking_repository:
    def __init__(self, conexion):
        self.conexion = conexion

    def save(self, booking):
        query = ("INSERT INTO booking (booking_id, checkin, checkout, service_name, price, id, name , last_name, phone, email, password, status, origin, occupation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        params = (
            booking.booking_id,
            booking.checkin,
            booking.checkout,
            booking.service_name,
            booking.price,
            booking.id,
            booking.name,
            booking.last_name,
            booking.phone,
            booking.email,
            booking.password,
            booking.status,
            booking.origin,
            booking.occupation
        )

        self.conexion.execute_query(query, params)