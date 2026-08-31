class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        num_freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            num_freq[c].append(n)

        final_arr = []

        for freq_arr in num_freq[::-1]:
            if k <= len(freq_arr):
                final_arr += freq_arr[0:k]
                return final_arr
            else:
                final_arr += freq_arr
                k -= len(freq_arr)

        return final_arr


            
        
        