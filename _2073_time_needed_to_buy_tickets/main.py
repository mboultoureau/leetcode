class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        count = 0

        while queue:
            ticket = queue.popleft() - 1
            if k == 0 and ticket == 0:
                return count + 1

            count += 1

            if ticket > 0:
                queue.append(ticket)

            if k == 0:
                k = len(queue) - 1
            else:
                k -= 1
