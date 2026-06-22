class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for c in s1: hashmap[c] = hashmap.get(c, 0) + 1
        count = len(s1)
        l = 0
        for r, char in enumerate(s2):
            while l < r and (char not in hashmap or hashmap[char] <= 0):
                if s2[l] in hashmap:
                    hashmap[s2[l]] += 1
                    count += 1
                l += 1
            if char in hashmap:
                hashmap[char] -= 1
                count -= 1
                if count == 0: return True
        return False
