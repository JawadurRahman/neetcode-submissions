from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            heapq.heappush(arr, (-x**2 - y**2, [x, y]))
            if len(arr) > k: heapq.heappop(arr)
        return [xy for _,xy in arr]