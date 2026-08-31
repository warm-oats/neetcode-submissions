class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hashmap = {')':'(', '}':'{', ']':'['}
        bracket_stack = []

        for char in s:
            if char in bracket_hashmap.values():
                bracket_stack.append(char)
            elif not bracket_stack:
                return False
            else:
                newest_open_bracket = bracket_stack.pop()

                if newest_open_bracket != bracket_hashmap[char]:
                    return False

        return not bracket_stack
        