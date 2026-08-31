import functools

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_hashmap = defaultdict(list)

        for i in range(len(nums) - 1):
            num_hashmap[i] += nums[i+1::]

        for i in range(len(nums) - 1, 0, -1):
            num_hashmap[i] += nums[0:i]


        res = []

        for arr in num_hashmap.values():
            arr_sum = functools.reduce(lambda a, b: a * b, arr)

            res.append(arr_sum)

        return res

