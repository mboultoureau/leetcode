class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // With NeetCode video solution help
        int result = 1;

        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back(make_pair(position[i], speed[i]));
        }
        sort(cars.rbegin(), cars.rend());

        double maxTime = (double)(target - cars[0].first) / (double)cars[0].second;
        for (int i = 1; i < cars.size(); i++) {
            double time = (double)(target - cars[i].first) / (double)cars[i].second;
            if (time > maxTime) {
                maxTime = time;
                result++;
            }
        }

        return result;
    }
};