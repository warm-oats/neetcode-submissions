class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        suffix_arr = []

        for pre_i in range(len(nums)):
            if pre_i == 0:
                prefix_arr.append(1)
            else:
                prefix_arr.append(nums[pre_i-1] * prefix_arr[-1])

        for suff_i in range(len(nums)-1,-1,-1):
            if suff_i == len(nums) - 1:
                suffix_arr.append(1)
            else:
                suffix_arr.append(nums[suff_i+1] * suffix_arr[-1])

        suffix_arr = suffix_arr[::-1]

        for i in range(len(suffix_arr)):
            prefix_arr[i] *= suffix_arr[i]

        return prefix_arr
