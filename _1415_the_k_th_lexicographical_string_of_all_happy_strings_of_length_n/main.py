class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0

        def backtracking(i, current, n, k):
            nonlocal count

            # End of the string
            if i == n:
                count += 1
                if k == count:
                    return ''.join(current)
                else:
                    return ''

            # All posibilities
            for c in ['a', 'b', 'c']:
                if c == current[-1]:
                    continue

                current.append(c)
                result = backtracking(i + 1, current, n, k) 
                current.pop()

                if result != '':
                    return result

            return ''

        return backtracking(0, [''], n, k)