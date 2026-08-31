class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [set() for _ in range(len(nums))]
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

        for num in nums:
            bucket[count[num] - 1].add(num)

        i = len(bucket) - 1

        while k > 0:
            res += list(bucket[i])
            k -= len(bucket[i])
            i -= 1
        
        return res

