class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(arr, index):
            if index >= len(nums):
                ans.append(arr)
                return

            dfs(arr, index + 1)
            arr2 = arr.copy()
            arr2.append(nums[index])
            dfs(arr2, index + 1)

        dfs([], 0)
        return ans

