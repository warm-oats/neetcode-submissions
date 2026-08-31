class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []

        if digits == '':
            return []

        def backtrack(curr_substr: str, digit_index: int):
            if digit_index >= len(digits):
                res.append(curr_substr)
                return

            mapped_letters = digits_map[digits[digit_index]]

            for letter in mapped_letters:
                curr_substr += letter
                backtrack(curr_substr, digit_index + 1)
                curr_substr = curr_substr[:-1]

        backtrack('', 0)

        return res

        