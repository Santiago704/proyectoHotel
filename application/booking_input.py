
class booking_input:
    def __init__(self):
        pass

    def add_booking(self, booking_service):
        try:
            checkin = input("Digite la fecha de ingreso al hotel: ")
            checkout = input("Digite la fecha de salida del hotel: ")
            room = input("Digite la habitación a reservar")
            booking_service.allow_booking(
                checkin, checkout
            )
            print(f"La habitacion {room} fue reservada con exito")
        except Exception as e:
            print("Error ", e)