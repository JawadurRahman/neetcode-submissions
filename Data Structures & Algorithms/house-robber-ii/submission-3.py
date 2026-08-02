class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cache = {}
        cache2 = {}

        def dfs(index):
            if index in cache: return cache[index]
            if index >= len(nums): return 0
            cache[index] = nums[index] + max(dfs(index + 2), dfs(index + 3))
            return cache[index]

        def dfs0(index):
            if index in cache2: return cache2[index]
            if index >= len(nums) - 1: return 0
            cache2[index] = nums[index] + max(dfs0(index + 2), dfs0(index + 3))
            return cache2[index]
            
        return max(dfs(1), dfs0(0), dfs(2))
