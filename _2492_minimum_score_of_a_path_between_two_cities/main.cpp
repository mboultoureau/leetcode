class Solution {
public:
    int find(auto& parent, int i)
    {
        if (parent[i] == i)
        {
            return i;
        }

        parent[i] = find(parent, parent[i]);
        return parent[i];
    }

    int minScore(int n, vector<vector<int>>& roads) {
        // Second solution: Union-find
        int result = std::numeric_limits<int>::max();
        std::vector<int> parent(n + 1);
        std::iota(parent.begin(), parent.end(), 0);

        for (const auto& road : roads)
        {
            parent[find(parent, road[0])] = find(parent, road[1]);
        }

        for (const auto& road : roads)
        {
            if (find(parent, road[0]) == find(parent, 1))
            {
                result = min(result, road[2]);
            }
        }

        return result;

        // First solution
        // struct Group
        // {
        //     int minimum { numeric_limits<int>::max() };
        //     unordered_set<int> cities;
        // };

        // // Associate each city to group
        // int groupId = 0;
        // std::unordered_map<int, int> cities;
        // std::unordered_map<int, Group> groups;

        // for (const auto& road : roads)
        // {
        //     int cityA = road[0];
        //     int cityB = road[1];
        //     int distance = road[2];

        //     if (!cities.contains(cityA) && !cities.contains(cityB))
        //     {
        //         groups[groupId] = {
        //             .minimum = distance,
        //             .cities = { cityA, cityB }
        //         };
        //         cities[cityA] = groupId;
        //         cities[cityB] = groupId;

        //         groupId++;
        //     }
        //     else if (cities.contains(cityA) && !cities.contains(cityB))
        //     {
        //         int cityGroupId = cities[cityA];
        //         groups[cityGroupId].minimum = min(groups[cityGroupId].minimum, distance);
        //         groups[cityGroupId].cities.insert(cityB);
        //         cities[cityB] = cityGroupId;
        //     }
        //     else if (!cities.contains(cityA) && cities.contains(cityB))
        //     {
        //         int cityGroupId = cities[cityB];
        //         groups[cityGroupId].minimum = min(groups[cityGroupId].minimum, distance);
        //         groups[cityGroupId].cities.insert(cityA);
        //         cities[cityA] = cityGroupId;
        //     }
        //     else
        //     {
        //         int cityAGroupId = cities[cityA];
        //         int cityBGroupId = cities[cityB];
                
        //         groups[cityAGroupId].minimum = min(groups[cityAGroupId].minimum, distance);

        //         if (cityAGroupId == cityBGroupId)
        //         {
        //             continue;
        //         }

        //         // Merge if different group
        //         groups[cityAGroupId].minimum = min(groups[cityAGroupId].minimum, groups[cityBGroupId].minimum);

        //         for (const auto& city : groups[cityBGroupId].cities)
        //         {
        //             cities[city] = cityAGroupId;
        //         }

        //         groups[cityAGroupId].cities.merge(groups[cityBGroupId].cities);
        //         groups.erase(cityBGroupId);
        //     }
        // }

        // // Get group of city 1
        // return groups[cities[1]].minimum;
    }
};