class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(word_arr: List[str], s_index: int):
            if s_index >= len(s):
                if word_arr[-1] == word_arr[-1][::-1]:
                    res.append(word_arr.copy())
                    
                return

            if len(word_arr) == 0 or word_arr[-1] == word_arr[-1][::-1]:
                word_arr.append(s[s_index])
                backtrack(word_arr, s_index + 1)
                word_arr.pop()

            if word_arr:
                word_arr[-1] = word_arr[-1] + s[s_index]

                backtrack(word_arr, s_index + 1)

        backtrack([], 0)

        return res