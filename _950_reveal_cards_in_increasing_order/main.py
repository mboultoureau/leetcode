class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0 for _ in range(len(deck))]
        queue = deque(range(len(deck)))

        for n in deck:
            i = queue.popleft()
            result[i] = n

            if queue:
                queue.append(queue.popleft())

        return result