class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        nums.sort()

        def dfs(index):
            if index >= len(nums):
                ans.append(temp.copy())
                return

            temp.append(nums[index])
            dfs(index + 1)

            temp.pop()
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1)
        dfs(0)
        return ans