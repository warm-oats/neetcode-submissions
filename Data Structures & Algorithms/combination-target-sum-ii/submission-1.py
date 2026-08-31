class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr_nums: List[int], num_index: int):
            if sum(curr_nums) == target and curr_nums not in res:
                res.append(curr_nums)
                return

            if num_index >= len(candidates) or sum(curr_nums) > target:
                return

            sorted_curr_nums = sorted(curr_nums + [candidates[num_index]])

            backtrack(sorted_curr_nums, num_index + 1)
            backtrack(curr_nums, num_index + 1)

        backtrack([], 0)
        
        return res