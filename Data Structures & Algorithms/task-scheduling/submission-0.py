import _heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        dq = deque([None]*n)
        heap = [(-count, task) for task, count in taskCounter.items()]
        heapq.heapify(heap)
        tasks = {task for task in taskCounter.keys()}
        cycles = 0
        while tasks:
            addedTaskToDq = False
            if heap:
                c, t = heapq.heappop(heap)
                c += 1
                if c != 0:
                    dq.append((c, t))
                    addedTaskToDq = True
                else:
                    tasks.remove(t)

            if not addedTaskToDq:
                dq.append(None)
            popped = dq.popleft()
            if popped:
                heapq.heappush(heap, popped)
            cycles += 1

        return cycles