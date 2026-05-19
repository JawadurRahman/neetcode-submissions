class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        heap = []
        for num, freq in hashmap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
        