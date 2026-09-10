class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cur_i = 0

        while True:
            if not nums[cur_i]:
                return cur_i
            
            temp = nums[cur_i]
            nums[cur_i] = None
            cur_i = temp

        