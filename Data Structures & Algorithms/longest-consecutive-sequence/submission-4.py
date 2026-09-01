class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            cur_seq = 0
            cur_num = 0

            if (num - 1) not in nums_set:
                cur_num = num
                
                while cur_num in nums_set:
                    cur_seq += 1
                    cur_num += 1

            longest_seq = max(longest_seq, cur_seq)
        
        return longest_seq