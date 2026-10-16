class Solution {
public:
    int countDigits(int n) {
        int count = 0;

        while (n != 0) {
            count++;
            n /= 10;
        }

        return count;
    }

    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        int longuest = 0;
        unordered_set<int> prefixes;

        for (auto n : arr1) {
            while (n != 0) {
                prefixes.insert(n);
                n /= 10;
            }
        }

        for (auto n : arr2) {
            while (n != 0) {
                if (prefixes.contains(n)) {
                    longuest = max(longuest, countDigits(n));
                    break;
                }
                
                n /= 10;
            }
        }

        return longuest;
    }
};