class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Solution 2
        s = s.replace('-', '').upper()
        groups = []

        if len(s) % k != 0:
            groups.append(s[:len(s) % k])

        for i in range(len(s) // k):
            groups.append(s[i * k + len(s) % k: i * k + len(s) % k + k])

        return "-".join(groups)

        # Solution 1
        # groups = []
        # current = ""

        # # Iterate from the end
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == '-':
        #         continue

        #     current = s[i].upper() + current
        #     if len(current) == k:
        #         groups.append(current)
        #         current = ""

        # if current != "":
        #     groups.append(current)

        # groups.reverse()

        # return '-'.join(groups)