class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_stonks = [-1] * len(nums)
        
        def recursion(index: int):
            if index >= len(nums):
                return 0

            if rob_stonks[index] != -1:
                return rob_stonks[index]

            rob_stonks[index] = max(nums[index] + recursion(index + 2), recursion(index + 1))

            return rob_stonks[index]

        return recursion(0)