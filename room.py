class Room:
    """Room class to manage hotel rooms."""

    def __init__(self, room_number, room_type, price_per_night, amenities):
        self.__room_number = room_number
        self.__type = room_type
        self.__price_per_night = price_per_night
        self.__amenities = amenities

    # Getter methods
    def get_room_number(self):
        return self.__room_number

    def get_type(self):
        return self.__type

    def get_price_per_night(self):
        return self.__price_per_night

    def get_amenities(self):
        return self.__amenities

    # Setter methods
    def set_type(self, room_type):
        self.__type = room_type

    def set_price_per_night(self, price):
        self.__price_per_night = price

    def set_amenities(self, amenities):
        self.__amenities = amenities


    def check_availability(self):
        """Check if room is available"""
        return True

    def get_room_details(self):
        """Get detailed information about room"""
        details = f"Room {self.__room_number}, Type: {self.__type}, Price: ${self.__price_per_night}"
        return details

    def update_status(self, status):
        """Update room status (example: occupied, maintenance)"""
        print(f"Room {self.__room_number} status updated to {status}")
        return True

    def get_amenities(self):
        return self.__amenities

    def __str__(self):
        return f"Room {self.__room_number}: {self.__type}, ${self.__price_per_night}/night, Amenities: {self.__amenities}"
