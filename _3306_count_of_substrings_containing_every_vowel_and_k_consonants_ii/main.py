class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.countOfSubstringsWithMinK(word, k) - self.countOfSubstringsWithMinK(word, k + 1)

    def countOfSubstringsWithMinK(self, word: str, k: int) -> int:
        left = 0
        right = 0
        substrings = 0
        vowels = defaultdict(int)
        vowels_count = 0
        consonants = 0

        while right < len(word):
            # Track vowels and consonants
            if word[right] in ['a', 'e', 'i', 'o', 'u']:
                vowels[word[right]] += 1
                if vowels[word[right]] == 1:
                    vowels_count += 1
            else:
                consonants += 1
            
            while vowels_count == 5 and consonants >= k:
                substrings += len(word) - right
                if word[left] in ['a', 'e', 'i', 'o', 'u']:
                    vowels[word[left]] -= 1
                    if vowels[word[left]] == 0:
                        vowels_count -= 1
                else:
                    consonants -= 1

                left += 1

            right += 1
            
        return substrings 