class GuestService:
    """GuestService class to manage additional services for guests."""

    def __init__(self, service_id, booking, service_type, status="Pending"):
        """Initialize guest service with details"""
        self.__service_id = service_id
        self.__booking = booking
        self.__service_type = service_type
        self.__status = status

    # Getter methods
    def get_service_id(self):
        return self.__service_id

    def get_booking(self):
        return self.__booking

    def get_service_type(self):
        return self.__service_type

    def get_status(self):
        return self.__status

    # Setter methods
    def set_service_type(self, service_type):
        self.__service_type = service_type

    def set_status(self, status):
        self.__status = status


    def request_service(self):
        """Request a new service"""
        self.__status = "Requested"
        print(f"Service {self.__service_id} ({self.__service_type}) requested")
        return True

    def track_request(self):
        """Track the status of service request"""
        return f"Service {self.__service_id} status: {self.__status}"

    def cancel_request(self):
        """Cancel service request"""
        if self.__status != "Completed":
            self.__status = "Cancelled"
            print(f"Service {self.__service_id} cancelled")
            return True
        else:
            print("Cannot cancel completed service")
            return False

    def __str__(self):
        return f"Service {self.__service_id}: {self.__service_type}, Status: {self.__status}"
