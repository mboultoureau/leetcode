class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int minimum = arrays[0][0];
        int maximum = arrays[0][arrays[0].size() - 1];
        int best = 0;

        for (int i = 1; i < arrays.size(); i++)
        {
            best = std::max(best, std::abs(maximum - arrays[i][0]));
            best = std::max(best, std::abs(arrays[i][arrays[i].size() - 1] - minimum));
            minimum = std::min(minimum, arrays[i][0]);
            maximum = std::max(maximum, arrays[i][arrays[i].size() - 1]);
        }

        return best;
    }
};