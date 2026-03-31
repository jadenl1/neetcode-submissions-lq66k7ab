class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True
        
        return False