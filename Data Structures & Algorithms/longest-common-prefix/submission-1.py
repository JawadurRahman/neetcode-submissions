class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        endIndix = len(prefix)
        for st in strs:
            i = 0
            while i < endIndix and i < len(st) and prefix[i] == st[i]: i += 1
            endIndix = i

        return prefix[0:endIndix]