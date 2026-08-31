class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        start_nums = set()
        seq_nums = set()
        longest_seq = 0

        for num in num_set:
            if (num - 1) in num_set:
                seq_nums.add(num)
            else:
                start_nums.add(num)

        for start_num in start_nums:
            current_seq = 1
            largest_num = start_num

            while (largest_num + 1) in seq_nums:
                largest_num += 1
                current_seq += 1
            
            longest_seq = max(longest_seq,current_seq)

        return longest_seq


        