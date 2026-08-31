class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1

        while end_index >= start_index:
            middle_index = math.floor((start_index + end_index) / 2)

            if nums[middle_index] > target:
                end_index = middle_index - 1
            elif nums[middle_index] < target:
                start_index = middle_index + 1 
            else:
                return middle_index
        
        return -1

