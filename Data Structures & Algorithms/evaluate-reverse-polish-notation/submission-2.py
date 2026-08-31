class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # the operators will always follow the numbers 
        # an operation will always occur when there are 3 indices

        # loop thru the array
        # if encounter number: push to a stack
        # if encounter operator: pop 2 from stack and perform operation
        # push res back into stack until full iteration through tokens list
        # return operands_stack[0]

        operands_stack = []

        for token in tokens:
            try:
                operands_stack.append(int(token))
            except:
                val2 = operands_stack.pop()
                val1 = operands_stack.pop()

                match token:
                    case '+':
                        operands_stack.append(self.plus(val1, val2))
                    case '-':
                        operands_stack.append(self.sub(val1, val2))
                    case '*':
                        operands_stack.append(self.mult(val1, val2))
                    case '/':
                        operands_stack.append(self.div(val1, val2))
            
        return operands_stack[-1]

    def plus(self, val1, val2):
        return val1 + val2

    def sub(self, val1, val2):
        return val1 - val2

    def mult(self, val1, val2):
        return val1 * val2
    
    def div(self, val1, val2):
        res = val1 / val2

        if res > 0:
            return math.floor(res)
        else:
            return math.ceil(res)