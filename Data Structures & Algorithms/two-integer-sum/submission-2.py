class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hashmap = {}

        for index in range(len(nums)):
            if (target - nums[index]) not in num_hashmap.keys():
                num_hashmap[nums[index]] = index
            else:
                return [num_hashmap[target - nums[index]], index]


        