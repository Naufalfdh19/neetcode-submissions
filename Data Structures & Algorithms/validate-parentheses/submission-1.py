class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0