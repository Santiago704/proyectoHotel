class booking_repository:
    def __init__(self, conexion):
        self.conexion = conexion

    def save(self, booking_obj):
        query = (
            "INSERT INTO booking (booking_id, guest_id, bedroom_id, service_id, checkin, checkout) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        params = (
            booking_obj.booking_id,
            booking_obj.guest_id,
            booking_obj.bedroom_id,
            booking_obj.service_id,
            booking_obj.checkin.isoformat(),
            booking_obj.checkout.isoformat(),
        )
        self.conexion.execute_query(query, params)