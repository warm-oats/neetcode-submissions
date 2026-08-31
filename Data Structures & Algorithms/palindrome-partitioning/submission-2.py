class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(curr_arr: List[str], char_index: int): 
            if char_index >= len(s):
                if curr_arr[-1] == curr_arr[-1][::-1]:
                    res.append(curr_arr.copy())
                return

            if curr_arr[-1] == curr_arr[-1][::-1]:
                curr_arr.append(s[char_index])
                backtrack(curr_arr, char_index + 1)
                curr_arr.pop()
            
            curr_arr[-1] += s[char_index]
            backtrack(curr_arr, char_index + 1)

        backtrack([s[0]], 1)

        return res