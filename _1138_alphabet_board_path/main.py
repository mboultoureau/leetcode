class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def getPath(source, destination):
            result = ""
            zDestination = False

            if source[0] == 5 and destination[0] != 5:
                source = (4, 0)
                result += 'U'

            if destination[0] == 5 and source[0] != 5:
                zDestination = True
                destination = (4, 0)

            # Top
            if source[0] > destination[0]:
                result += "U" * (source[0] - destination[0])

            # Down
            else:
                result += "D" * (destination[0] - source[0])

            # Left
            if source[1] > destination[1]:
                result += "L" * (source[1] - destination[1])

            # Right
            else:
                result += "R" * (destination[1] - source[1])

            if zDestination:
                result += 'D'

            result += "!"
            return result
        
        result = ""
        source = (0, 0)
        for c in target:
            index = ord(c) - ord('a')
            destination = (index // 5, index % 5)
            result += getPath(source, destination)
            source = destination

        return result