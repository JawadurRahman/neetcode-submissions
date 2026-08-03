class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = set()
        def bfs():
            dq = deque([0])
            count = 0
            if 0 == amount: return 0

            while dq:
                for _ in range(len(dq)):
                    prevTotal = dq.popleft()
                    if prevTotal in cache: continue
                    cache.add(prevTotal)
                    for c in coins:
                        if c + prevTotal > amount: continue
                        if c + prevTotal == amount: return count + 1
                        dq.append(c + prevTotal)
                count += 1
            return -1
                
        return bfs()