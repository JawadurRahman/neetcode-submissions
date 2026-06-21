class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        length = 0
        leftIndex = 0
        if s == "": return 0
        for rightIndex, char in enumerate(s):
            while char in hashset:
                hashset.remove(s[leftIndex])
                leftIndex += 1
            hashset.add(char)
            length = max(length, rightIndex - leftIndex)

        return length + 1