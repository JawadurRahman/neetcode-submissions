class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s.lower():
            if c.isalnum():
                arr.append(c)
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - 1 - i]: return False
        return True