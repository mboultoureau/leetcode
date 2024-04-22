class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        visited.add("0000")
        queue = deque(["0000"])
        steps = 0

        if "0000" in deadends:
            return -1

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node == target:
                    return steps

                for neighbor in self.getNeighbors(node):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            steps += 1

        return -1

    def getNeighbors(self, code: str) -> List[str]:
        units = int(code[3])
        tens = int(code[2])
        hundreds = int(code[1])
        thousands = int(code[0])

        neighbors = []
        neighbors.append(f"{thousands}{hundreds}{tens}{(units + 1) % 10}")
        neighbors.append(f"{thousands}{hundreds}{tens}{(units - 1) % 10}")
        neighbors.append(f"{thousands}{hundreds}{(tens + 1) % 10}{units}")
        neighbors.append(f"{thousands}{hundreds}{(tens - 1) % 10}{units}")
        neighbors.append(f"{thousands}{(hundreds + 1) % 10}{tens}{units}")
        neighbors.append(f"{thousands}{(hundreds - 1) % 10}{tens}{units}")
        neighbors.append(f"{(thousands + 1) % 10}{hundreds}{tens}{units}")
        neighbors.append(f"{(thousands - 1) % 10}{hundreds}{tens}{units}")

        return neighbors

