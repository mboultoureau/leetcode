class Solution {
public:
    string minWindow(string s, string t) {
        if (t.size() > s.size())
        {
            return "";
        }

        // Much faster than classic hashmap
        int target[128] = {0};
        int current[128] = {0};
        int nb = 0;
        int bestLeft = 0;
        int bestLength = INT_MAX;
        int left = 0;
        int right = 0;
        
        // Fill target hashmap
        for (int i = 0; i < t.size(); i++)
        {
            target[t.at(i)]++;
        }

        while (left < s.size())
        {
            // Increment right until match or end
            while (nb != t.size() && right < s.size())
            {
                current[s.at(right)]++;
                if (current[s.at(right)] <= target[s.at(right)])
                {
                    nb++;
                }
                right++;
            }

            // Best match
            if (nb == t.size() && right - left < bestLength)
            {
                bestLeft = left;
                bestLength = right - left;
            }
            

            // Optimization
            current[s.at(left)]--;
            if (current[s.at(left)] < target[s.at(left)])
            {
                nb--;
                left++;
                continue;
            }

            left++;
        }
        
        if (bestLength == INT_MAX)
        {
            return "";
        }
        else
        {
            return s.substr(bestLeft, bestLength);
        }
    }
};