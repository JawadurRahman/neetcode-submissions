class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for w in strs:
            s = ''.join(sorted(w))
            if s not in hashmap:
                hashmap[s] = [w]
            else:
                hashmap[s].append(w)
        
        return list(hashmap.values())
