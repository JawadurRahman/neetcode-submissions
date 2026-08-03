class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            string = ""
            stringRev = ""
            for j in range(i, len(s)):
                string = string + s[j]
                stringRev = s[j] + stringRev
                if string == stringRev and len(string) > len(ans):
                    ans = string

        return ans