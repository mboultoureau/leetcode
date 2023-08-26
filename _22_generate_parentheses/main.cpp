class Solution {
public:
    void backtrack(int n, int open, int close, string sequence, vector<string>& result) {
        if (open == close && close == n) {
            result.push_back(sequence);
            return;
        }

        if (open < n) {
            sequence.push_back('(');
            backtrack(n, open + 1, close, sequence, result);
            sequence.pop_back();
        }

        if (close < open) {
            sequence.push_back(')');
            backtrack(n, open, close + 1, sequence, result);
            sequence.pop_back();
        }
    }


    vector<string> generateParenthesis(int n) {
        vector<string> result;

        backtrack(n, 1, 0, "(", result);

        return result;
    }
};