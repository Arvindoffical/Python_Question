class MyCalendar:

    def __init__(self):
        self.bookings = []  # List to store booked intervals

    def book(self, start: int, end: int) -> bool:
        # Loop through existing bookings to check for overlap
        for existingStart, existingEnd in self.bookings:
            # Check if new event overlaps with an existing one
            if start < existingEnd and end > existingStart:
                return False
        
        # No overlap, add the event to the list of bookings
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)