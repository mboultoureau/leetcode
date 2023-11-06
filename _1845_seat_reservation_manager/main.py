import bisect

class SeatManager:
    # Solution 2
    def __init__(self, n: int):
        self.availableSeats = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.availableSeats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.availableSeats, seatNumber)


    # Solution 1
    # def __init__(self, n: int):
    #     self.availableSeats = list(range(1, n + 1))

    # def reserve(self) -> int:
    #     return self.availableSeats.pop(0)

    # def unreserve(self, seatNumber: int) -> None:
    #     bisect.insort(self.availableSeats, seatNumber) 


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)