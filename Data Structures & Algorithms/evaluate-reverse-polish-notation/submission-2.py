class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack, push numbers

        stack = []

        ops = ["+", "-", "*", "/"]

        for token in tokens:
            # if non-number
            if token in ops:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if token == "+":
                    stack.append(int(operand1 + operand2))
                elif token == "-":
                    stack.append(int(operand1 - operand2))
                elif token == "*":
                    stack.append(int(operand1 * operand2))
                elif token == "/":
                    stack.append(int(operand1 / operand2))
            else:
                #number, push to stack
                stack.append(int(token))
        
        return stack[0]
