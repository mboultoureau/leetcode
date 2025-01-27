class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        outputs = defaultdict(set)

        for a, b in prerequisites:
            outputs[a].add(b)

        visited = set()
        def bfs(current, target, visited):
            if current in visited:
                return False

            if current == target:
                return True

            visited.add(current)
            found = False
            for neighbor in outputs[current]:
                if bfs(neighbor, target, visited):
                    found = True
                    break

            return found
            

        result = []
        for a, b in queries:
            result.append(bfs(a, b, set()))

        return result