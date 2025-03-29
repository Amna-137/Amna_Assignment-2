class Booking:
    """Booking class to manage hotel reservations."""

    def __init__(self, booking_id, guest, room, check_in_date, check_out_date, status="Confirmed"):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status

    # Getter methods
    def get_booking_id(self):
        return self.__booking_id

    def get_guest(self):
        return self.__guest

    def get_room(self):
        return self.__room

    def get_check_in_date(self):
        return self.__check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def get_status(self):
        return self.__status

    # Setter methods
    def set_check_in_date(self, date):
        self.__check_in_date = date

    def set_check_out_date(self, date):
        self.__check_out_date = date

    def set_status(self, status):
        self.__status = status


    def create_booking(self):
        """Create a new booking"""
        print(f"Booking created: ID {self.__booking_id}")
        return True

    def cancel_booking(self):
        """Cancel an existing booking"""
        self.__status = "Cancelled"
        print(f"Booking {self.__booking_id} has been cancelled")
        return True

    def modify_booking(self):
        """Modify booking details"""
        print(f"Booking {self.__booking_id} has been modified")
        return True

    def generate_invoice(self):
        """Generate invoice for the booking"""
        from invoice import Invoice
        invoice = Invoice(self.__booking_id, self.__guest, self.__room,
                          self.__check_in_date, self.__check_out_date)
        return invoice

    def __str__(self):
        return (f"Booking {self.__booking_id}: Guest {self.__guest.get_name()}, "
                f"Room {self.__room.get_room_number()}, Check-in: {self.__check_in_date}, "
                f"Check-out: {self.__check_out_date}, Status: {self.__status}")
