class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0

        while i < len(tokens):
            if len(stack) < 2:
                stack.append(tokens[i])
                i += 1
                continue
            if tokens[i] not in "+-/*":
                stack.append(tokens[i])
                i += 1
                continue
            
            b = stack.pop()
            a = stack.pop()
            op = tokens[i]
            ans = None
            if op == "+":
                ans = int(a) + int(b)
            elif op == "-":
                ans = int(a) - int(b)
            elif op == "/":
                ans = int(int(a) / int(b))
            elif op == "*":
                ans = int(a) * int(b)
            i += 1
            stack.append(ans)

        return int(stack[0])