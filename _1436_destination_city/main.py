class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = defaultdict(int)
        for path in paths:
            cities[path[0]] += 1
            cities[path[1]] += 2

        for city, value in cities.items():
            if value == 2:
                return city

        return None
