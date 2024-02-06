class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            key = list(str)
            key.sort()
            map[''.join(key)].append(str)

        result = []
        for key in map:
            anagrams = []
            for str in map[key]:
                anagrams.append(str)

            result.append(anagrams)

        return result