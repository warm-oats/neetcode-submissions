class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_operators = ['+','-','*','/']
        num_stack = []

        for token in tokens:
            if token in math_operators:
                operand_2 = int(num_stack.pop())
                operand_1 = int(num_stack.pop())

                match token:
                    case '+':
                        num_stack.append(operand_1 + operand_2)
                    case '-':
                        num_stack.append(operand_1 - operand_2)
                    case '*':
                        num_stack.append(operand_1 * operand_2)
                    case '/':
                        num_stack.append(operand_1 / operand_2)
            else:
                num_stack.append(token)
        
        return int(num_stack[0])