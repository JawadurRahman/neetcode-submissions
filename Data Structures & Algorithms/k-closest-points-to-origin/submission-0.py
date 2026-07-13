from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            heapq.heappush(arr, (x**2 + y**2, [x, y]))

        return [heapq.heappop(arr)[1] for i in range(k)]