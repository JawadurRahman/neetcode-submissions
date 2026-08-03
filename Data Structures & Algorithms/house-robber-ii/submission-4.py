class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cache = {}

        def dfs(index, limit):
            if (index, limit) in cache: return cache[(index, limit)]
            if index >= limit: return 0
            cache[(index, limit)] = nums[index] + max(dfs(index + 2, limit), dfs(index + 3, limit))
            return cache[(index, limit)]
            
        return max(dfs(1, len(nums)), dfs(0, len(nums) - 1), dfs(2, len(nums)))