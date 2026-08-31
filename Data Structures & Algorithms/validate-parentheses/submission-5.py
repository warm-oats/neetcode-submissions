class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        paren_hashmap = {']':'[','}':'{',')':'('}

        for parenthesis in s:
            if parenthesis in paren_hashmap.values():
                paren_stack.append(parenthesis)
            elif len(paren_stack) == 0 or paren_hashmap[parenthesis] != paren_stack.pop():
                    return False

        return len(paren_stack) == 0 
