class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(prefix_stack: List[int], i: int):
            if i >= len(nums):
                return

            curr_stack = [nums[i]]

            # Choose to add prefix + value at index
            combined_stack = prefix_stack + curr_stack
            res.append(combined_stack)
            backtrack(combined_stack, i + 1)

            # Choose not to add value at index
            backtrack(prefix_stack, i + 1)

        backtrack([], 0)

        return res
