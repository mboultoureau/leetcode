class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int depth{};
        vector<int> result;

        for (char c : seq) {
            if (c == '(')
            {
                depth++;
                result.push_back(depth % 2);
            }
            else
            {
                result.push_back(depth % 2);
                depth--;
            }
        }

        return result;
    }
};