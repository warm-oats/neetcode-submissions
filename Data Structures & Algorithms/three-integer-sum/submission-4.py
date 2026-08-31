class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # num2 + num3 = -num1

        for index_num1 in range(len(nums)): # target 
            if index_num1 > 0 and nums[index_num1] == nums[index_num1 - 1]:
                continue

            pointer_start = index_num1 + 1
            pointer_end = len(nums) - 1

            while pointer_end > pointer_start:
                three_sum = nums[pointer_start] + nums[pointer_end] + nums[index_num1]

                if three_sum > 0:
                    pointer_end -= 1
                elif three_sum < 0:
                    pointer_start += 1
                else:
                    res.append([nums[index_num1],nums[pointer_start],nums[pointer_end]])
                    pointer_start += 1 

                    while nums[pointer_start] == nums[pointer_start - 1] and pointer_start < pointer_end:
                        pointer_start += 1 

        return res

