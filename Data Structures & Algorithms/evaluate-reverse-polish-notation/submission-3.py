class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = [] # add numbers onto stack, once we get an operator, pop two perform it, then push result back
        # stack should be empty by the end

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                if len(stack) >= 2:
                    op1 = stack.pop() # right op
                    op2 = stack.pop()
                    
                if tokens[i] == "+":
                    res = op1 + op2
                elif tokens[i] == "-":
                    res = op2 - op1
                elif tokens[i] == "*":
                    res = op1 * op2
                elif tokens[i] == "/":
                    if op1 != 0:
                        res = int(op2/op1)
                stack.append(res)
                

        return stack[-1]
