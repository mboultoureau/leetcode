class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> matchingParentheses = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };

        stack<char> stack;

        for (int i = 0; i < s.size(); i++) {
            if (matchingParentheses.find(s.at(i)) != matchingParentheses.end()) {
                stack.push(s.at(i));
            } else if (!stack.empty() && matchingParentheses[stack.top()] == s.at(i)) {
                stack.pop();
            } else {
                return false;
            }
        }

        return stack.empty();
    }
};