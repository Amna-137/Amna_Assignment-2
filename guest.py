class Guest:
    """Guest class to store information about hotel guests."""

    def __init__(self, name, email, phone, loyalty_status="Regular"):
        """Initialize a guest with personal information"""
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__loyalty_status = loyalty_status

    # Getter methods
    def get_name(self):

        return self.__name

    def get_email(self):

        return self.__email

    def get_phone(self):

        return self.__phone

    def get_loyalty_status(self):

        return self.__loyalty_status

    # Setter methods
    def set_name(self, name):

        self.__name = name

    def set_email(self, email):

        self.__email = email

    def set_phone(self, phone):

        self.__phone = phone

    def set_loyalty_status(self, status):

        self.__loyalty_status = status


    def create_account(self):
        print(f"Account created for {self.__name}")
        return True

    def update_profile(self):
        print(f"Profile updated for {self.__name}")
        return True

    def view_reservation_history(self):
        history = f"Reservation history for {self.__name}"
        return history

    def __str__(self):
        return f"Guest: {self.__name}, Email: {self.__email}, Phone: {self.__phone}, Status: {self.__loyalty_status}"

