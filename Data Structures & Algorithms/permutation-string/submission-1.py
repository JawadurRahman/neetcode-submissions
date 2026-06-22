class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for c in s1: hashmap[c] = hashmap.get(c, 0) + 1
        count = len(s1)
        l = 0
        for r, char in enumerate(s2):
            if char not in hashmap:
                l = r
                hashmap = {}
                for c in s1: hashmap[c] = hashmap.get(c, 0) + 1
                continue
            while char in hashmap and hashmap[char] <= 0:
                if s2[l] in hashmap:
                    hashmap[s2[l]] += 1
                l += 1
            hashmap[char] -= 1
                
            if sum(list(hashmap.values())) == 0: return True
        return False
