class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        previous = 0

        for row in bank:
            count = row.count('1')
            if count == 0:
                continue

            result += count * previous
            previous = count
            

        return result