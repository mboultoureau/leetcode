class Solution:
    def isPathCrossing(self, path: str) -> bool:
        crossings = defaultdict(list)
        current = [0, 0]

        crossings[0].append(0)

        for p in path:
            if p == 'N':
                current[1] += 1
            elif p == 'S':
                current[1] -= 1
            elif p == 'E':
                current[0] += 1
            else:
                current[0] -= 1

            if current[0] in crossings and current[1] in crossings[current[0]]:
                return True
            else:
                crossings[current[0]].append(current[1])

        return False