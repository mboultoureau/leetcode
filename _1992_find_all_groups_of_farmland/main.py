class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        result = []

        def dfs(y, x, land, current):
            nonlocal result

            # Check if bottom left
            if land[y + 1][x] == 0 and land[y][x + 1] == 0:
                current.extend([y, x])
                result.append(current)

                for row in range(current[0], current[2] + 1):
                    for col in range(current[1], current[3] + 1):
                        land[row][col] = 0

                return

            # Go to bottom if possible
            if land[y + 1][x] == 1:
                dfs(y + 1, x, land, current)
            else:
                dfs(y, x + 1, land, current)


        for y in range(len(land)):
            land[y].append(0)

        land.append([0 for _ in range(len(land[0]))])

        for y in range(len(land)):
            for x in range(len(land[0])):
                if land[y][x] == 1:
                    dfs(y, x, land, [y, x])

        return result