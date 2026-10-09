class Solution {
private:
    std::vector<int> parent;
    std::vector<size_t> size;
    size_t count{};

public:
    int find(int city) {
        while (city != parent[city]) {
            parent[city] = parent[parent[city]];
            city = parent[city];
        }

        return city;
    }

    void merge(int city1, int city2) {
        int root1 = find(city1);
        int root2 = find(city2);

        if (root1 == root2) {
            return;
        }

        if (size[root1] > size[root2]) {
            parent[root2] = root1;
            size[root1] += size[root2];
        } else {
            parent[root1] = root2;
            size[root2] += size[root1];
        }

        count--;
    }


    int findCircleNum(vector<vector<int>>& isConnected) {
        // Union-Find
        int n = isConnected.size();

        parent.reserve(n);
        size.reserve(n);

        for (int i = 0; i < n; ++i) {
            parent.push_back(i);
            size.push_back(1);
            count++;
        }

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isConnected[i][j] == 1) {
                    merge(i, j);
                }
            }
        }

        return count;
    }
};