class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_start, ans_len = 0, 0

        for i in range(len(s)):
            l = i
            r = i

            length = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if length > ans_len:
                    ans_start = l
                    ans_len = length
                l -= 1
                r += 1
                length += 2

            l = i
            r = i + 1
            length = 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if length > ans_len:
                    ans_start = l
                    ans_len = length
                l -= 1
                r += 1
                length += 2 

        return s[ans_start: ans_start + ans_len]