class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                new_sum = nums[i] + nums[j] + nums[k]
                sorted_arr = sorted([nums[i], nums[j], nums[k]])

                if new_sum == 0 and sorted_arr not in res:
                    res.append(sorted_arr)

                if new_sum > 0:
                    k -= 1
                else:
                    j += 1
        
        return res

