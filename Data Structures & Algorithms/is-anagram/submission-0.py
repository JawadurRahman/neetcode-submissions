class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = Counter()
        tset = Counter()
        for c in s:
            hashset[c] += 1
        for c in t:
            tset[c] += 1
        return tset == hashset
            
        
