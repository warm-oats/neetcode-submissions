class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_num = None
        post_num = None
        final_arr = []

        for prefix in nums:
            if pre_num == None:
                pre_num = prefix
                final_arr.append(1)
            else:
                final_arr.append(pre_num)
                pre_num *= prefix

        for index in range(-1,-(len(nums)+1),-1):
            if post_num == None:
                post_num = nums[index]
            else:
                final_arr[index] *= post_num
                post_num *= nums[index]

        return final_arr
        
                
