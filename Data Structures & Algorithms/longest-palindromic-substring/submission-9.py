class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_start, ans_len = 0, 0

        def isPalindrome():
            lo, hi = i, j
            is_palindrome = True
            while lo < hi:
                if s[lo] != s[hi]:
                    is_palindrome = False
                    break
                lo += 1
                hi -= 1

            return is_palindrome

        for i in range(len(s)):
            for j in range(i, len(s)):
                length = j - i + 1
                if length <= ans_len:
                    continue  # can't possibly beat current best, skip the check

                if isPalindrome():
                    ans_start, ans_len = i, length

        return s[ans_start: ans_start + ans_len]