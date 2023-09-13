class Solution {
public:
    int characterReplacement(string s, int k) {
        // With the help of Neetcode video solution
        array<int, 26> letters = {0}; // Way faster than hashmap

        int left = 0;
        int right = 0;
        int maxLength = 0;
        int maxFrequency = 0;

        while (right < s.size())
        {
            letters[s[right] - 'A']++;
            if (letters[s[right] - 'A'] > maxFrequency)
            {
                maxFrequency = letters[s[right] - 'A'];
            }

            // Is current window valid?
            if ((right - left + 1) - maxFrequency > k)
            {
                letters[s[left] - 'A']--;
                left++;
            }

            maxLength = max(right - left + 1, maxLength);
            right++;
        }

        return maxLength;
    }
};