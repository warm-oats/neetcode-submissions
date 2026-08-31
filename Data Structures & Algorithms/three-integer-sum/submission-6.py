class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # num2 + num3 = -num1
        for index,num1 in enumerate(nums):
            start_index = index + 1
            end_index = len(nums) - 1

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            while end_index > start_index:
                current_sum = nums[start_index] + nums[end_index]

                if current_sum > -num1:
                    end_index -= 1
                elif current_sum < -num1:
                    start_index += 1
                else:
                    res.append([num1,nums[start_index],nums[end_index]])
                    start_index += 1
                    
                    while nums[start_index] == nums[start_index - 1] and end_index > start_index:
                        start_index += 1
        
        return res