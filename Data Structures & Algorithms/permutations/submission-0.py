class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr_nums, curr_nums_len, num_index):
            if curr_nums_len == len(nums):
                res.append(curr_nums.copy())
                return
            if num_index >= len(nums):
                return
            
            for i in range(len(curr_nums)):
                if curr_nums[i] == -20:
                    curr_nums[i] = nums[num_index]
                    backtrack(curr_nums, curr_nums_len + 1, num_index + 1)
                    curr_nums[i] = -20

        backtrack([-20] * len(nums), 0, 0)

        return res
                