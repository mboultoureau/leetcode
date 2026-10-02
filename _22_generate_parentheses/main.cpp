class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generate(n, n, "", result);
        return result;
    }

    void generate(int remainingLeft, int remainingRight, string current, vector<string>& result) {
        if (remainingLeft == 0 && remainingRight == 0) {
            result.push_back(current);
            return;
        }

        // Left
        if (remainingLeft != 0) {
            generate(remainingLeft - 1, remainingRight, current + "(", result);
        }

        // Right
        if (remainingLeft < remainingRight) {
            generate(remainingLeft, remainingRight - 1, current + ")", result);
        }
    }
};