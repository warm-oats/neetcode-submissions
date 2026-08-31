class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sequence_starts = set()
        sequence_nums = set()
        longest_seq_count = 0

        for num in num_set:
            if (num - 1) not in num_set:
                sequence_starts.add(num)
            else:
                sequence_nums.add(num)

        for seq_start in sequence_starts:
            if (longest_seq_count == 0):
                longest_seq_count = 1

            increment = 1

            while (increment != -1):
                if (seq_start + increment) in sequence_nums:
                    increment += 1
                else:
                    longest_seq_count = max(increment, longest_seq_count)
                    increment = -1

        return longest_seq_count
        