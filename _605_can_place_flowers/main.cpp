class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // With Neetcode video
        if (n == 0) return true;

        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);

        for (int i = 1; i < flowerbed.size() - 1; i++)
        {
            if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)
            {
                flowerbed[i] = 1;
                n--;
            }

            if (n == 0)
            {
                return true;
            }
        }

        return false;

        // My solution
        // if (n == 0)
        // {
        //     return true;
        // }

        // int i = 1;
        // int number = 0;

        // if (flowerbed.size() == 1 && flowerbed[0] == 0)
        // {
        //     number++;
        //     flowerbed[0] = 1;
        // }

        // if (flowerbed[0] == 0 && flowerbed.size() >= 2 && flowerbed[1] == 0)
        // {
        //     number++;
        //     flowerbed[0] = 1;
        // }

        // while (i < flowerbed.size() - 1)
        // {
        //     if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)
        //     {
        //         number++;
        //         flowerbed[i] = 1;
        //     }

        //     i++;
        // }

        // if (flowerbed.size() >= 2 && flowerbed[flowerbed.size() - 1] == 0 && flowerbed[flowerbed.size() - 2] == 0)
        // {
        //     number++;
        //     flowerbed[flowerbed.size() - 1] = 1;
        // }

        // return number >= n;
    }
};