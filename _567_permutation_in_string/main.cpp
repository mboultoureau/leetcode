class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        // With Neetcode video solution
        if (s2.size() < s1.size())
        {
          return false;
        }

        int matches = 0;
        
        array<int, 26> s1Count = {0};
        array<int, 26> s2Count = {0};
        for (int i = 0; i < s1.size(); i++)
        {
          s1Count[s1[i] - 'a']++;
          s2Count[s2[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++)
        {
            if (s1Count[i] == s2Count[i])
            {
                matches++;
            }
        }

        if (matches == 26)
        {
            return true;
        }

        for (int left = 0; left < s2.size() - s1.size(); left++)
        {
            // Modify left
            if (s1Count[s2[left] - 'a'] == s2Count[s2[left] - 'a'])
            {
                matches--;
            }
            s2Count[s2[left] - 'a']--;
            if (s1Count[s2[left] - 'a'] == s2Count[s2[left] - 'a'])
            {
                matches++;
            }

            // Modify right
            int right = left + s1.size();
            if (s1Count[s2[right] - 'a'] == s2Count[s2[right] - 'a'])
            {
                matches--;
            }
            s2Count[s2[right] - 'a']++;
            if (s1Count[s2[right] - 'a'] == s2Count[s2[right] - 'a'])
            {
                matches++;
            }

            if (matches == 26)
            {
                return true;
            }
        }

        return false;
    }
};