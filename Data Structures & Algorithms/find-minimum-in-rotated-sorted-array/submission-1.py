class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = None
        iteration = 0

        while r >= l:
            middle = math.floor((r + l) / 2)

            if nums[middle] > nums[r]:
                l = middle + 1
            elif nums[middle] <= nums[r]:
                r = middle - 1
                
            min_num = nums[middle] if (iteration == 0) else min(min_num, nums[middle])
            iteration += 1
        
        return min_num


