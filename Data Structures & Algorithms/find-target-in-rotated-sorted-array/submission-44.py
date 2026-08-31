class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1

        while end_index >= start_index:
            middle_index = math.floor((start_index + end_index) / 2)

            if nums[middle_index] == target:
                return middle_index

            if nums[start_index] <= nums[middle_index]:
                if target > nums[middle_index] or target < nums[start_index]:
                    start_index = middle_index + 1
                else:
                    end_index = middle_index - 1
            elif nums[start_index] > nums[middle_index]:
                if target > nums[end_index] or target < nums[middle_index]:
                    end_index = middle_index - 1
                else:
                    start_index = middle_index + 1
        
        return -1      