class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - num1 = num2 
        num_hashmap = defaultdict(int)

        for i,num in enumerate(nums):
            if (target - num) not in num_hashmap:
                num_hashmap[num] = i
            else:
                return [num_hashmap[target - num],i]






        