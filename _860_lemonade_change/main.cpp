class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        std::array<int, 3> change = {0, 0, 0};
        for (int bill : bills)
        {
            switch (bill)
            {
                case 5:
                    change[0] += 1;
                    break;
                case 10:
                    change[1] += 1;
                    change[0] -= 1;
                    if (change[0] < 0)
                        return false;
                    break;
                case 20:
                    change[2] += 1;
                    if (change[1] > 0 and change[0] > 0)
                    {
                        change[1] -= 1;
                        change[0] -= 1;
                    }
                    else if (change[0] >= 3)
                    {
                        change[0]  -= 3;
                    }
                    else
                    {
                        return false;
                    }
                    break;
            }
        }

        return true;
    }
};