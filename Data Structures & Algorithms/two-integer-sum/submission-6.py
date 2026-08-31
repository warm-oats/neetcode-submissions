class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found_hash = defaultdict(int)
        
        for i in range(len(nums)):
            operand = target - nums[i]

            if operand in found_hash:
                return [found_hash[operand], i]
            
            found_hash[nums[i]] = i
