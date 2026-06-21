class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = defaultdict(int)
        hashmap["A"] = 0
        length = 0
        for r, c in enumerate(s):
            hashmap[c] += 1
            vals = list(hashmap.values())
            vals.sort(reverse=True)
            while sum(vals) - vals[0] > k:
                hashmap[s[l]] -= 1
                l += 1
                vals = list(hashmap.values())
                vals.sort(reverse=True)
            length = max(length, sum(vals))
        return length


                
            
