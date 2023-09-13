class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Must faster than hashmaps
        vector<int> letters(127, -1);
        
        int left = 0;
        int right = 0;
        int maxLength = 0;

        while (right < s.size())
        {
            if (letters[s[right]] != -1)
            {
                while (left < letters[s[right]])
                {
                    letters[s[left]] = -1;
                    left++;
                }

                left = letters[s[right]] + 1;
            }

            letters[s[right]] = right;
            maxLength = max(right - left + 1, maxLength);

            right++;
        }

        return maxLength;
    }
};