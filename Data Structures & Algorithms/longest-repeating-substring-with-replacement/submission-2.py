class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = defaultdict(int)
        length = 0
        maxf = 0
        for r, c in enumerate(s):
            hashmap[c] += 1
            maxf = max(hashmap[c], maxf)
            while (r - l + 1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length


                
            
