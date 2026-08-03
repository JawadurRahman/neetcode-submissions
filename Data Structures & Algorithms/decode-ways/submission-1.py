class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {str(i) for i in range(1,27)}

        dp = [0] * len(s)
        dp.extend([1,1])
        for i in range(len(s) - 1, -1, -1):
            l1 = s[i]
            l2 = None
            if i < len(s) - 1: 
                l2 = s[i] + s[i + 1]
            if l1 in hmap: 
                dp[i] += dp[i + 1]
            if l2 in hmap: 
                dp[i] += dp[i + 2]
        return dp[0]