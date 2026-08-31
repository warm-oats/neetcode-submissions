class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]

        while r >= l:
            middle = math.floor((r + l) / 2)

            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle - 1
                
            min_num = min(min_num, nums[middle])
        
        return min_num


