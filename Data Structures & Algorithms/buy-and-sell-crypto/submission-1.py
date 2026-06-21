class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        r = 0
        while r < len(prices):
            ans = max(ans, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return ans