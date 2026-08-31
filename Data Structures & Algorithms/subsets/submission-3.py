class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(prefix_stack: List[int], i: int):
            if i >= len(nums):
                return

            curr_stack = prefix_stack + [nums[i]]

            # Choose to add prefix + value at index
            res.append(curr_stack)
            backtrack(curr_stack, i + 1)

            # Choose not to add value at index
            backtrack(prefix_stack, i + 1)

        backtrack([], 0)

        return res
