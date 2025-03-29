class Payment:
    """Payment class to handle financial transactions."""

    def __init__(self, payment_id, amount, payment_method):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__payment_method = payment_method

    # Getter methods
    def get_payment_id(self):
        return self.__payment_id

    def get_amount(self):
        return self.__amount

    def get_payment_method(self):
        return self.__payment_method

    # Setter methods
    def set_amount(self, amount):
        self.__amount = amount

    def set_payment_method(self, method):
        self.__payment_method = method


    def process_payment(self):
        """Process the payment """
        print(f"Payment {self.__payment_id} processed: ${self.__amount} via {self.__payment_method}")
        return True

    def apply_discount(self, discount_percent):
        """Apply discount to payment"""
        if 0 <= discount_percent <= 100:
            self.__amount = self.__amount * (1 - discount_percent / 100)
            print(f"Discount of {discount_percent}% applied. New amount: ${self.__amount}")
            return True
        return False

    def get_receipt(self):
        """Generate receipt for payment"""
        receipt = f"Receipt: Payment ID {self.__payment_id}, Amount: ${self.__amount}, Method: {self.__payment_method}"
        return receipt

    def __str__(self):
        return f"Payment {self.__payment_id}: ${self.__amount} via {self.__payment_method}"