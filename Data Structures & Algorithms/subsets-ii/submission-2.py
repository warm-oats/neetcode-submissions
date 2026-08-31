class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        def backtrack(curr_nums: List[int], num_index: int):
            if num_index >= len(nums):
                return

            curr_nums.append(nums[num_index])
            res.append(curr_nums.copy())
            backtrack(curr_nums, num_index + 1)
            curr_nums.pop()

            while num_index + 1 < len(nums) and nums[num_index] == nums[num_index + 1]:
                num_index += 1

            backtrack(curr_nums, num_index + 1)

        backtrack([], 0)

        return res