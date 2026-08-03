from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                string = s[i: j]
                if string == string[::-1] and len(string) > len(ans):
                    ans = string

        return ans