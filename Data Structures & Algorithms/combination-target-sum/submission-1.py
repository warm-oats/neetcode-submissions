class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr_nums: List[int], num_index: int):
            if sum(curr_nums) == target:
                res.append(curr_nums)
                return

            if num_index >= len(nums) or sum(curr_nums) > target:
                return

            nums_arr = []
            curr_sum = 0

            while curr_sum < target:
                if curr_sum == target:
                    res.append(nums_arr)

                nums_arr.append(nums[num_index])
                curr_sum += nums[num_index]

                backtrack(curr_nums + nums_arr, num_index + 1)

            backtrack(curr_nums, num_index + 1)

        backtrack([], 0)

        return res