class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substr_set = set()
        longest_substr_len = 0

        while l < len(s) and r < len(s):
            if s == "": return 0

            # Check with right pointer if char is in substr_set
            # If not: slide r over to the right
            # If it is, there is a repeat, update longest_subtr_len, set l = r, continue

            if s[r] not in substr_set:
                substr_set.add(s[r])
                r += 1
            else:
                substr_set = set()
                l += 1
                r = l

            longest_substr_len = max(longest_substr_len, len(substr_set))
            
        return longest_substr_len




        