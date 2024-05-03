class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = self.parse_version(version1)
        v2 = self.parse_version(version2)

        if len(v1) > len(v2):
            v2.extend([0 for _ in range(len(v1) - len(v2))])
        elif len(v1) < len(v2):
            v1.extend([0 for _ in range(len(v2) - len(v1))])

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0


    def parse_version(self, version) -> list[int]:
        result = []
        for rev in version.split('.'):
            result.append(int(rev))

        return result