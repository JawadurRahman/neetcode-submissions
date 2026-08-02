class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)
        for index in range(len(nums) -1, -1, -1):
            dp[index] = nums[index] + max(dp[index + 2], dp[index + 3])

        return max(dp[0], dp[1])