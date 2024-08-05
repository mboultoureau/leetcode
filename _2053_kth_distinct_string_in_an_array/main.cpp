class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        std::unordered_map<std::string, int> count;
        for (const std::string &str : arr)
        {
            if (count.contains(str))
            {
                count[str] += 1;
            }
            else
            {
                count[str] = 1;
            }
        }

        for (const std::string &str : arr)
        {
            if (count[str] != 1)
            {
                continue;
            }

            k--;
            if (k == 0)
            {
                return str;
            }
        }
        
        return "";
    }
};