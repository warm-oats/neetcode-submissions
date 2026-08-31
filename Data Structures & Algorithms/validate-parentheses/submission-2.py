class Solution:
    def isValid(self, s: str) -> bool:
        closed_chars = {')':'(', '}':'{', ']':'['}
        open_chars = ['(', '{', '[']
        chars_stack = []

        for char in s:
            if char in open_chars:
                chars_stack.append(char)
            else:
                if not chars_stack:
                    return False

                newest_open_char = chars_stack.pop()

                if newest_open_char != closed_chars[char]:
                    return False

        if not chars_stack:
            return True

        return False
        