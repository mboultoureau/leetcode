class TimeMap {
private:
public:
    unordered_map<string, vector<pair<int, string>>> data = {};

    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        auto it = data.find(key);
        if (it != data.end()) {
            it->second.push_back(make_pair(timestamp, value));
        } else {
            data[key] = vector<pair<int, string>>();
            data[key].push_back(make_pair(timestamp, value));
        }
    }
    
    string get(string key, int timestamp) {
        auto it = data.find(key);
        if (it == data.end()) {
            return "";
        }

        int left = 0;
        int right = it->second.size() - 1;

        pair<int, string> bestMatch = make_pair(0, "");

        while (left <= right) {
            int middle = (left + right) / 2;
            if (it->second[middle].first > timestamp) {
                right = middle - 1;
            } else {
                if (bestMatch.first <= timestamp) {
                    bestMatch = make_pair(timestamp, it->second[middle].second);
                }
                left = middle + 1;
            }
        }

        return bestMatch.second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */