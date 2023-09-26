class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() - 1;
        bool retenue;
        
        do {
            digits[i] = (digits[i] + 1) % 10;
            retenue = (digits[i] == 0);

            // Significant speed improvement
            if (!retenue)
            {
                return digits;
            }

            i--;
        } while (retenue && i >= 0);
        
        if (retenue)
        {
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};