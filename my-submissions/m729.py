class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        insertLocation = bisect_left(self.bookings, (start, end))

        # end of schedule
        if insertLocation >= len(self.bookings) :
            if not self.bookings :
                self.bookings.append((start, end))
                return True
            if start == self.bookings[-1][1] :
                self.bookings[-1] = (self.bookings[-1][0], end)
                return True
            if start < self.bookings[-1][1] :
                return False
            self.bookings.append((start, end))
            return True

        if insertLocation and start < self.bookings[insertLocation - 1][1] :
            return False
        if start == self.bookings[insertLocation][0] :
            return False
        if end == self.bookings[insertLocation][0] :
            self.bookings[insertLocation] = (start, self.bookings[insertLocation][1])
            return True
        if end > self.bookings[insertLocation][0] :
            return False

        self.bookings.insert(insertLocation, (start, end))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
