import _heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        dq = deque()
        heap = [-count for task, count in taskCounter.items()]
        heapq.heapify(heap)
        cycles = 0
        while dq or heap:
            if heap:
                c = heapq.heappop(heap)
                c += 1
                if c != 0: dq.append((c, cycles))

            if dq and dq[0][1] == cycles - n:
                heapq.heappush(heap, dq.popleft()[0])
            cycles += 1

        return cycles