class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        PandS = [(p, s, (target - p)/s) for p, s in zip(position, speed)]
        PandS.sort(key=lambda x: x[0])
        count = 1
        stack = []
        for x in PandS:
            while stack and stack[-1][2] <= x[2]:
                stack.pop()
            stack.append(x)   
        return len(stack)