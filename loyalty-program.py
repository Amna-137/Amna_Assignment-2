class LoyaltyProgram:
    """LoyaltyProgram class to manage guest rewards and benefits."""

    def __init__(self, guest, points=0, member_since=None):
        self.__guest = guest
        self.__points = points
        self.__member_since = member_since

    # Getter methods
    def get_guest(self):
        return self.__guest

    def get_points(self):
        """Return loyalty points"""
        return self.__points

    def get_member_since(self):
        return self.__member_since

    # Setter methods
    def set_points(self, points):
        self.__points = points

    def set_member_since(self, date):
        self.__member_since = date


    def earn_points(self, amount):
        """Add points to loyalty account"""
        prev_points = self.__points
        self.__points += amount
        print(f"Points added: {amount}. New balance: {self.__points}")
        return self.__points

    def redeem_points(self, points_to_redeem):
        """Redeem points for benefits"""
        if points_to_redeem <= self.__points:
            self.__points -= points_to_redeem
            print(f"Redeemed {points_to_redeem} points. Remaining: {self.__points}")
            return True
        else:
            print("Insufficient points")
            return False

    def check_status(self):
        """Check loyalty program status"""
        if self.__points < 500:
            status = "Silver"
        elif self.__points < 1000:
            status = "Gold"
        else:
            status = "Platinum"

        return f"Status: {status}, Points: {self.__points}, Member since: {self.__member_since}"

    def __str__(self):
        return f"Loyalty Program : {self.__guest.get_name()}, Points: {self.__points}, Member since: {self.__member_since}"
