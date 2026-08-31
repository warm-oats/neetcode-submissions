class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_items = defaultdict(int)
        freq_bucket = [[] for slot in range(len(nums))]
        final_arr = []

        for num in nums:
            count_items[num] += 1

        for key,value in count_items.items():
            freq_bucket[value - 1].append(key)

        for num_arr in freq_bucket[::-1]:
            if k <= len(num_arr):
                final_arr += num_arr[0:k]
                return final_arr
            else:
                final_arr += num_arr
                k -= len(num_arr)

        return final_arr

        

        


        

        