from functools import cache

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(index, sum):
            if sum > target:
                return

            if sum == target:
                ans.append(temp.copy())

            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(i, sum + nums[i])
                temp.pop()
        
        dfs(0, 0)
        return ans