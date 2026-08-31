class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        # Contrainst 1: Add open if openParens < n
        # Constraint 2: Add closed if openParens > closedParens

        def backtracking(openParens,closedParens):
            if openParens == closedParens == n:
                res.append(''.join(stack))
                return
                
            if openParens < n:
                stack.append('(')
                backtracking(openParens + 1,closedParens)
                stack.pop()
            
            if openParens > closedParens:
                stack.append(')')
                backtracking(openParens,closedParens + 1)
                stack.pop()
        
        backtracking(0,0)

        return res