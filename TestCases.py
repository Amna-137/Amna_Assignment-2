from guest import Guest
from room import Room
from booking import Booking
from payment import Payment
from invoice import Invoice
from loyalty_program import LoyaltyProgram
from guest_service import GuestService
from feedback import Feedback
if __name__ == "__main__":
    # Test 1: Create guest accounts
    print("--- Guest Account Creation Tests ---")
    # Create first guest
    g1 = Guest("Amna Fahed", "amna.fahed.05@gmail.com", "0566497977")
    g1.create_account()
    print(g1)
    
    # Create second guest with Gold status
    g2 = Guest("Saeed Fahed", "saeed2002@gmail.com", "0505126677", "Gold")
    g2.create_account()
    print(g2)
    
    # Test 2: Search for rooms
    print("--- Room Search Tests ---")
    # Create some rooms
    r1 = Room(101, "Standard", 100.0, "WiFi, TV")
    r2 = Room(102, "Standard", 100.0, "WiFi, TV, Fridge")
    r3 = Room(201, "Deluxe", 200.0, "WiFi, TV, Fridge")
    r4 = Room(301, "Suite", 300.0, "WiFi, TV, Kitchen, Jacuzzi")
    
    # Search for standard rooms
    print("Standard rooms:")
    rooms = [r1, r2, r3, r4]
    for r in rooms:
        if r.get_type() == "Standard":
            print(r.get_room_details())
    
    # Search for rooms with fridge
    print("Rooms with fridge:")
    for r in rooms:
        if "Fridge" in r.get_amenities():
            print(r.get_room_details())
    
    # Test 3: Make room bookings
    print("--- Room Booking Tests ---")
    # Book room 1 for guest 1
    b1 = Booking(1001, g1, r1, "2024-05-01", "2024-05-03")
    b1.create_booking()
    print(b1)
    
    # Book room 3 for guest 2
    b2 = Booking(1002, g2, r3, "2024-06-01", "2024-06-05")
    b2.create_booking()
    print(b2)
    
    # Test 4: Confirm bookings
    print("--- Booking Confirmation Tests ---")
    # Confirm first booking
    b1.set_status("Confirmed")
    print(f"Booking 1 status: {b1.get_status()}")
    print(f"Email sent to: {g1.get_email()}")
    
    # Confirm second booking
    b2.set_status("Confirmed")
    print(f"Booking 2 status: {b2.get_status()}")
    print(f"Email sent to: {g2.get_email()}")
    
    # Test 5: Generate invoices
    print("--- Invoice Generation Tests ---")
    # Generate invoice for booking 1
    inv1 = b1.generate_invoice()
    print(inv1)
    
    # Generate invoice for booking 2
    inv2 = b2.generate_invoice()
    print(inv2)
    
    # Test 6: Process payments
    print("--- Payment Processing Tests ---")
    # Process credit card payment
    p1 = Payment(5001, 200.0, "Credit Card")
    p1.process_payment()
    inv1.set_payment_details(p1)
    print(p1)
    print(f"Receipt: {p1.get_receipt()}")
    
    # Process mobile payment with discount
    p2 = Payment(5002, 800.0, "Mobile Payment")
    p2.process_payment()
    p2.apply_discount(10)  # 10% discount
    inv2.set_payment_details(p2)
    print(p2)
    print(f"Receipt: {p2.get_receipt()}")
    
    # Test 7: View reservation history
    print("--- Reservation History Tests ---")
    # View history for guest 1
    print(g1.view_reservation_history())
    
    # View history for guest 2
    print(g2.view_reservation_history())
    
    # Test 8: Cancel reservations
    print("--- Reservation Cancellation Tests ---")
    # Cancel booking 1
    print(f"Before cancellation: {b1}")
    b1.cancel_booking()
    print(f"After cancellation: {b1}")
    r1.update_status("Available")
    
    # Cancel booking with refund
    b3 = Booking(1003, g2, r4, "2024-07-01", "2024-07-03")
    b3.create_booking()
    p3 = Payment(5003, 600.0, "Credit Card")
    p3.process_payment()
    b3.cancel_booking()
    print(f"Refund processed: ${p3.get_amount()}")
    r4.update_status("Available")
    
    # Error handling tests
    print("--- Error Handling Tests ---")
    
    # Test invalid rating
    print("1. Testing invalid rating:")
    fb = Feedback(b2)
    good_rating = fb.submit_feedback(5)  # Valid rating
    bad_rating = fb.submit_feedback(6)   # Invalid rating
    print(f"Valid rating result: {good_rating}")
    print(f"Invalid rating result: {bad_rating}")
    
    # Test insufficient points
    print("2. Testing loyalty points:")
    lp = LoyaltyProgram(g1, 100, "2024-01-01")
    enough = lp.redeem_points(50)     # Should work
    not_enough = lp.redeem_points(200)  # Should fail
    print(f"Redeem 50 points result: {enough}")
    print(f"Redeem 200 points result: {not_enough}")
    
    # Test cancelling completed service
    print("3. Testing service cancellation:")
    service = GuestService(101, b2, "Room Service")
    service.request_service()
    service.set_status("Completed")
    cancel_result = service.cancel_request()
    print(f"Cancel completed service result: {cancel_result}")