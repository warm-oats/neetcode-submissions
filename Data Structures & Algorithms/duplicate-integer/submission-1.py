class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        index = 0

        for num in nums:
            if ((index + 1) >= len(nums)):
                return False

            if (num == nums[index + 1]):
                return True
            index += 1

        return False