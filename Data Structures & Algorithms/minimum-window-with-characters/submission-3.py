class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lettersRemaining = len(t)
        counter = Counter(t)
        ans = None
        lPtr = 0
        rPtr = 0

        for i in range(len(s)):
            if s[i] in counter:
                temp = defaultdict(int)
                for j in range(i, len(s)):
                    if s[j] in counter and temp[s[j]] != counter[s[j]]:
                        temp[s[j]] += 1
                        lettersRemaining -= 1
                    if lettersRemaining == 0 and (ans == None or len(ans) > j - i + 1):
                        ans = s[i:j+1]
                        break
                    if j == len(s) - 1 and lettersRemaining != 0:
                        return ans if ans else ""

                lettersRemaining = len(t)


        return ans if ans else ""
