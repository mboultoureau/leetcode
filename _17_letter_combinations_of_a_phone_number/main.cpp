class Solution {
public:
    std::vector<string> letterCombinations(std::string digits) {
        std::vector<string> solutions;

        if (digits.size() > 0)
        {
            backtracking(0, digits, solutions, "");
        }
    
        return solutions;
    }

private:
    void backtracking(int i, std::string& digits, std::vector<string>& solutions, std::string current)
    {
        if (i == digits.size())
        {
            solutions.push_back(current);
            return;
        }

        char digit = digits[i];

        for (const char& c : m_Mapping.at(digit))
        {
            current.push_back(c);
            backtracking(i + 1, digits, solutions, current);
            current.pop_back();
        }
    }

    const std::unordered_map<char, std::string> m_Mapping = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
};