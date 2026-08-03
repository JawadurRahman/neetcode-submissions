class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {str(i) for i in range(1,27)}

        dp1 = 1
        dp2 = 1
        for i in range(len(s) - 1, -1, -1):
            dp0 = 0
            l1 = s[i]
            l2 = None
            if i < len(s) - 1: l2 = s[i] + s[i + 1]
            if l1 in hmap: dp0 += dp1
            if l2 in hmap: dp0 += dp2
            dp2 = dp1
            dp1 = dp0

        return dp1