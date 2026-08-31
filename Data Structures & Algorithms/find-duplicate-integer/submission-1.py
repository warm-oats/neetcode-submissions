class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow = 0, 0
        slow_2 = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                while slow != slow_2:
                    slow = nums[slow]
                    slow_2 = nums[slow_2]
                else:
                    return slow


            