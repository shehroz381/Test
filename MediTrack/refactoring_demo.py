import sqlite3

#ORIGINAL INEFFICIENT CODE
def get_patient_bookings(patient_id):
    conn = sqlite3.connect('meditrack.db')
    cursor = conn.cursor()
    
    # Get all booking IDs first
    cursor.execute("SELECT id FROM bookings WHERE patient_id = ?", (patient_id,))
    booking_ids = cursor.fetchall()
    
    # ❌ Problem: One query PER booking (N+1 problem)
    bookings = []
    for booking_id in booking_ids:
        cursor.execute("SELECT * FROM bookings WHERE id = ?", (booking_id[0],))
        booking = cursor.fetchone()
        bookings.append(booking)
    
    conn.close()
    return bookings


#  FINAL OPTIMIZED CODE
def get_patient_bookings_optimized(patient_id):
    with sqlite3.connect('meditrack.db') as conn:
        cursor = conn.cursor()
        # Single query fetches ALL bookings at once
        cursor.execute("SELECT * FROM bookings WHERE patient_id = ?", (patient_id,))
        bookings = cursor.fetchall()
    return bookings