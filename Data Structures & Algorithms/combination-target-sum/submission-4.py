class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []

        def dfs(index, sum):
            if sum == target:
                ans.append(temp.copy())
                return
            if index >= len(nums) or sum + nums[index] > target:
                return

            temp.append(nums[index])
            dfs(index, sum + nums[index])
            temp.pop()
            dfs(index + 1, sum)

        dfs(0, 0)
        return ans