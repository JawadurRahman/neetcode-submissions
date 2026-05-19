class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        lt = [(k, v) for k, v in hashmap.items()]
        print(lt)
        lt.sort(reverse=True, key=lambda x: x[1])
        return [i for i,j in lt][:k]