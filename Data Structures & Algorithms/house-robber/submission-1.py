class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index):
            if index in cache: return cache[index]
            if index >= len(nums): return 0
            cache[index] = nums[index] + max(dfs(index + 2), dfs(index + 3))
            return cache[index]
            
        return max(dfs(0), dfs(1))