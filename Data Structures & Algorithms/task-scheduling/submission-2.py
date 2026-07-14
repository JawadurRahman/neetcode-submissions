import _heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dq = deque()
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        cycles = 0
        
        while dq or heap:
            if heap:
                c = heapq.heappop(heap) + 1
                if c != 0: dq.append((c, cycles))
            else: cycles = dq[0][1] + n

            if dq and dq[0][1] == cycles - n:
                heapq.heappush(heap, dq.popleft()[0])
            cycles += 1

        return cycles