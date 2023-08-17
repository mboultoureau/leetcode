class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        unsigned int nbAccounts = accounts.size();
        unsigned int nbBanks = accounts[0].size();

        unsigned int maxWealth = 0;
        unsigned int customerWealth = 0;

        for (unsigned int i = 0; i < nbAccounts; i++) {
            customerWealth = 0;
            for (unsigned int j = 0; j < nbBanks; j++) {
                customerWealth += accounts[i][j];
            }

            if (customerWealth > maxWealth) {
                maxWealth = customerWealth;
            }
        }

        return maxWealth;
    }
};