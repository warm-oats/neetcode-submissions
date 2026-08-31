class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(curr_nums: List[int], num_index: int, total: int):
            if total == target:
                res.append(curr_nums.copy())
                return

            if num_index >= len(candidates) or total > target:
                return

            curr_nums.append(candidates[num_index])
            backtrack(curr_nums, num_index + 1, total + candidates[num_index])
            curr_nums.pop()

            while (num_index + 1) < len(candidates) and candidates[num_index] == candidates[num_index + 1]:
                num_index += 1

            backtrack(curr_nums, num_index + 1, total)

        backtrack([], 0, 0)
        
        return res