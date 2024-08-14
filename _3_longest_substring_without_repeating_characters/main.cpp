class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::array<int, 128> letters;
        std::fill(letters.begin(), letters.end(), -1);
        int start = 0;
        int result = 0;

        for (int i = 0; i < s.size(); i++)
        {
            char letter = s[i];

            if (letters[letter] != -1)
            {
                for (int j = start; j < letters[letter]; j++)
                {
                    letters[j] = -1;
                }
                start = max(start, letters[letter] + 1);
            }

            result = max(result, i - start + 1);
            letters[letter] = i;
        }

        return result;



        // Must faster than hashmaps
        // vector<int> letters(127, -1);
        
        // int left = 0;
        // int right = 0;
        // int maxLength = 0;

        // while (right < s.size())
        // {
        //     if (letters[s[right]] != -1)
        //     {
        //         while (left < letters[s[right]])
        //         {
        //             letters[s[left]] = -1;
        //             left++;
        //         }

        //         left = letters[s[right]] + 1;
        //     }

        //     letters[s[right]] = right;
        //     maxLength = max(right - left + 1, maxLength);

        //     right++;
        // }

        // return maxLength;
    }
};