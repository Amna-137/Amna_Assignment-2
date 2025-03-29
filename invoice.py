class Invoice:
    """Invoice class to manage billing information."""

    def __init__(self, invoice_id, guest, room, check_in_date, check_out_date):
        self.__invoice_id = invoice_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__payment_details = None

    # Getter methods
    def get_invoice_id(self):
        return self.__invoice_id

    def get_payment_details(self):
        return self.__payment_details

    # Setter methods
    def set_payment_details(self, payment):
        self.__payment_details = payment


    def generate_invoice(self):
        """Generate the invoice document"""
        print(f"Invoice {self.__invoice_id} generated for guest {self.__guest.get_name()}")
        return True

    def __str__(self):
        """String representation of invoice"""
        if self.__payment_details:
            payment_info = f", Payment: ${self.__payment_details.get_amount()}"
        else:
            payment_info = ", Payment: Pending"

        return (f"Invoice {self.__invoice_id}: Guest {self.__guest.get_name()}, "
                f"Room {self.__room.get_room_number()}, "
                f"Period: {self.__check_in_date} to {self.__check_out_date}{payment_info}")
