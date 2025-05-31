class booking_input:
    def __init__(self):
        pass

    def add_booking(self, booking_service):
        try:
            checkin_string = input("Digite la fecha de ingreso al hotel (dd-mm-yyyy): ")
            checkout_string = input("Digite la fecha de salida del hotel (dd-mm-yyyy): ")
            room = input("Digite la habitación a reservar: ")

            booking_service.allow_booking(checkin_string, checkout_string, room)

            print(f"La habitación {room} fue reservada con éxito")
        except Exception as e:
            print("Error ", e)