class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')':
                if not stack or (stack and stack.pop() != '('):
                    return False
            elif c == '}':
                if not stack or (stack and stack.pop() != '{'):
                    return False
            elif c == ']':
                if not stack or (stack and stack.pop() != '['):
                    return False
        
        if stack and len(stack) > 0:
            return False
        
        return True