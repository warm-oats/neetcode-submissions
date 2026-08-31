class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        # Constraint 1: Add open if openParens < n
        # Constraint 2: Add closed if openParens > n

        def backtrack(openParens, closedParens):
            if openParens == closedParens == n:
                res.append(''.join(stack))
                return 

            if openParens < n:
                stack.append('(')
                backtrack(openParens + 1, closedParens)
                stack.pop()

            if openParens > closedParens:
                stack.append(')')
                backtrack(openParens, closedParens + 1)
                stack.pop()

        backtrack(0, 0)

        return res