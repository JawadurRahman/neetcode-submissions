class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)
        for index in range(len(nums) -1, -1, -1):
            dp[index] =  max(nums[index] + dp[index + 2], dp[index + 1])

        return dp[0]