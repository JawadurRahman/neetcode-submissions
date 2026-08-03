class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            string = ""
            for j in range(i, len(s)):
                string = string + s[j]
                if string == string[::-1] and len(string) > len(ans):
                    ans = string

        return ans