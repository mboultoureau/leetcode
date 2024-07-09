class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 1
        total = 0

        for customer in customers:
            start = max(time, customer[0])
            end = start + customer[1]
            total += end - customer[0]
            time = end

        return total / len(customers)