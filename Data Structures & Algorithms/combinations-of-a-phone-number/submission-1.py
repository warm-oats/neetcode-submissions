class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        res = []

        if not digits:
            return res

        def backtrack(cur_substr: str, digit_index: int):
            if digit_index >= len(digits):
                res.append(cur_substr)
                return

            for letter in digit_map[int(digits[digit_index])]:
                cur_substr += letter
                backtrack(cur_substr, digit_index + 1)
                cur_substr = cur_substr[:-1]

        backtrack('', 0)

        return res

            