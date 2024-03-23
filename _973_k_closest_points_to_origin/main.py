class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(points)):
            point = points[i]
            heapq.heappush(heap, (-sqrt(point[0] ** 2 + point[1] ** 2), i))

        result = []
        for _, i in heapq.nlargest(k, heap):
            result.append(points[i])

        return result