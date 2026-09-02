class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_1 = 0
        op_2 = 0
        stack = []
        operations = ['-','+','/','*']

        if len(tokens) <= 2:
            return int(tokens[0])

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                op_2 = stack.pop()
                op_1 = stack.pop()
                
                match token:
                    case '+':
                        op_1 += op_2
                    case '-':
                        op_1 -= op_2
                    case '*':
                        op_1 *= op_2
                    case '/':
                        op_1 /= op_2
                
                stack.append(int(op_1))
        
        return stack[0]

