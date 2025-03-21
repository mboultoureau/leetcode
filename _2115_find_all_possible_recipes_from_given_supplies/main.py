class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        result = []
        supplies = set(supplies)
        lastCount = -1
        queue = deque(range(len(recipes)))

        while len(supplies) > lastCount:
            lastCount = len(supplies)
            queueCount = len(queue)

            while queueCount > 0:
                i = queue.popleft()
                valid = True
                for ing in ingredients[i]:
                    if ing not in supplies:
                        valid = False
                        break

                if valid:
                    supplies.add(recipes[i])
                    result.append(recipes[i])
                else:
                    queue.append(i)


                queueCount -= 1

        return result