class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'}':'{', ']':'[', ')':'('}
        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        
        return not stack