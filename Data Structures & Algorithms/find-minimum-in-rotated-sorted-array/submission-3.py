class Solution:
    def findMin(self, nums: List[int]) -> int:
        start_index, end_index = 0, len(nums) - 1
        min_num = None

        # Check if array is not rotated
        if nums[start_index] < nums[end_index] or len(nums) == 1:
            return nums[start_index]

        while end_index >= start_index:
            middle_index = math.floor((start_index + end_index) / 2)
            
            if nums[middle_index] > nums[-1]:
                start_index = middle_index + 1
            else:
                index = middle_index

                while index > 0 and nums[index - 1] < nums[index]:
                    index -= 1

                min_num = nums[index]
                break

        return min_num
             