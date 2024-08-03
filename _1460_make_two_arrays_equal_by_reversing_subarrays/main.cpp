class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        std::array<int, 1000> count;
	    std::fill(count.begin(), count.end(), 0);
        for (const int& c : target) {
		    count[c - 1] += 1;
	    }

        for (const int& c : arr) {
            count[c - 1] -= 1;
        }

        for (const int& value : count) {
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
};
