class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            prev = max(prev + n, n)
            ans = max(prev, ans)

        return ans