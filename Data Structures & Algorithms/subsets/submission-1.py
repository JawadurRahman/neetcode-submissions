class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(i):
            if i >= len(nums):
                ans.append(temp.copy())
                return

            temp.append(nums[i])
            dfs(i + 1)

            temp.pop()
            dfs(i + 1)
        dfs(0)
        return ans
