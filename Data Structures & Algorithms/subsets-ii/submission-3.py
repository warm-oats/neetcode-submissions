class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(num_arr: List[int], num_index: int):
            if num_index >= len(nums):
                res.append(num_arr.copy())
                return

            if not num_arr or num_arr[-1] != nums[num_index]:
                backtrack(num_arr, num_index + 1)

            num_arr.append(nums[num_index])
            backtrack(num_arr, num_index + 1)
            num_arr.pop()

        backtrack([], 0)

        return res