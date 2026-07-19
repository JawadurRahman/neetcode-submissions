class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lettersRemaining = len(t)
        counter = Counter(t)
        ans = None
        lPtr = 0
        rPtr = 0

        for i in range(len(s)):
            if s[i] in counter:
                for j in range(i, len(s)):
                    if s[j] in counter and counter[s[j]] > 0:
                        counter[s[j]] -= 1
                        lettersRemaining -= 1
                    if lettersRemaining == 0 and (ans == None or len(ans) > j - i + 1):
                        ans = s[i:j+1]
                counter = Counter(t)
                lettersRemaining = len(t)


        return ans if ans else ""
