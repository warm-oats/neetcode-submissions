class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.helper(res, nums, [])

        return res
    
    def helper(self, res, nums, cur_nums):
        if (not nums):
            res.append(list(cur_nums))
            return

        self.helper(res, nums[1::], list(cur_nums))
        
        cur_nums.append(nums[0])
        
        self.helper(res, nums[1::], list(cur_nums))

        


