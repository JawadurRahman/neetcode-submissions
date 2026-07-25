from functools import cache

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(index, sum):
            if sum > target or index >= len(nums):
                return

            if sum == target:
                ans.append(temp.copy())
                return

            temp.append(nums[index])
            if sum + nums[index] <= target:
                dfs(index, sum + nums[index])
            temp.pop()
            dfs(index + 1, sum)

        
        dfs(0, 0)
        return ans