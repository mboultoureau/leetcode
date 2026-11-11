class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long long total = 0;
        
        // If cost both is too expensive, drop it
        if (costBoth >= cost1 + cost2) {
            return static_cast<long long>(cost1) * need1 + static_cast<long long>(cost2) * need2;
        }

        // Buy until one is full
        int nbBuy = min(need1, need2);
        total += static_cast<long long>(costBoth) * nbBuy;
        need1 -= nbBuy;
        need2 -= nbBuy;

        // Buy remaining
        if (need1 > 0) {
            total += static_cast<long long>(min(cost1, costBoth)) * need1;
        } else if (need2 > 0) {
            total += static_cast<long long>(min(cost2, costBoth)) * need2;
        }

        return total;
    }
};