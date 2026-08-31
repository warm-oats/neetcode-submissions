class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(word_arr: List[str], s_index: int):
            if s_index >= len(s):
                if word_arr[-1] == word_arr[-1][::-1]:
                    res.append(word_arr.copy())

                return

            if word_arr[-1] == word_arr[-1][::-1]:
                word_arr.append(s[s_index])
                backtrack(word_arr, s_index + 1)
                word_arr.pop()

            word_arr[-1] += s[s_index]
            backtrack(word_arr, s_index + 1)

        backtrack([s[0]], 1)

        return res