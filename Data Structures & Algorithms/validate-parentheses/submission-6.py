class Solution:
    def isValid(self, s: str) -> bool:
        friends = {"}":"{", ")":"(", "]":"["}
        
        stack = []
        for char in s:
            #open, (
            if char in friends.values():
                stack.append(char)
            #close, )
            else:
                # match it to its open
                if stack and stack[-1] == friends[char]:
                    stack.pop()
                else:
                    return False
                            
        if len(stack) == 0:
            return True
        else:
            return False