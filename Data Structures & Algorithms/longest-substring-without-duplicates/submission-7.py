class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = 0
        end_index = 0
        substr_set = set()
        longest_substr_count = 0

        while end_index < len(s):
            if s[end_index] not in substr_set:
                substr_set.add(s[end_index])
                end_index += 1
            else:
                start_index += 1
                end_index = start_index
                substr_set = set()

            longest_substr_count = max(longest_substr_count,(end_index - start_index))

        return longest_substr_count
            