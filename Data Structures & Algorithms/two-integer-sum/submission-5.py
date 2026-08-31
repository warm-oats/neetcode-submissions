class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_set = defaultdict(int) # key: num, value: index

        for i in range(0, len(nums)):
            if target - nums[i] in num_set:
                return [num_set[target - nums[i]], i]

            num_set[nums[i]] = i






        