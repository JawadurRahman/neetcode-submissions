class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack and stack[-1] == '(' and c == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and c == ']':
                stack.pop()
            elif stack and stack[-1] == '{' and c == '}':
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
            