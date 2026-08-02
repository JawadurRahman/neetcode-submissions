from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def r(count):
            if count == n: return 1
            if count > n: return 0
            return r(count + 1) + r(count + 2)

        return r(0)

            