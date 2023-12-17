from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_to_cuisine = {}
        self.foods_to_rating = {}
        self.cuisines = defaultdict(SortedList)

        for i in range(len(foods)):
            self.foods_to_rating[foods[i]] = ratings[i]
            self.foods_to_cuisine[foods[i]] = cuisines[i]
            self.cuisines[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        currentRating = self.foods_to_rating[food]
        self.cuisines[self.foods_to_cuisine[food]].remove((-currentRating, food))
        self.foods_to_rating[food] = newRating
        self.cuisines[self.foods_to_cuisine[food]].add((-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)