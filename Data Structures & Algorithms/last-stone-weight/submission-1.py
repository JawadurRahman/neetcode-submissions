from _heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-s for s in stones]
        heapify(arr)
        while len(arr) > 1:
            a = -heappop(arr)
            b = -heappop(arr)
            w = abs(a - b)
            if w != 0:
                heappush(arr, -w)
            
        return 0 if not arr else -arr[0]