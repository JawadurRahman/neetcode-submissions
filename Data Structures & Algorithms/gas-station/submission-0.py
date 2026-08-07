class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        ans = -1

        while start < len(gas) and ans == -1:
            totalgas = 0
            for i in range(start, start + len(gas)):
                gasi = gas[i % len(gas)]
                totalgas += gasi
                costi = cost[i % len(cost)]
                totalgas -= costi
                if totalgas >= 0 and i == start + len(gas) - 1:
                    ans = start
                    break
                if totalgas < 0: 
                    start = i + 1
                    totalgas = 0

        return ans