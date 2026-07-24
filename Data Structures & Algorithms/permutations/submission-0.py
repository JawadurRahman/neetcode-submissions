class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        aSet = set()
        def dfs(i):
            if i >= len(nums):
                ans.append(temp.copy())

            for n in nums:
                if n not in aSet:
                    temp.append(n)
                    aSet.add(n)
                    dfs(i + 1)
                    aSet.remove(n)
                    temp.pop()

        dfs(0)
        return ans