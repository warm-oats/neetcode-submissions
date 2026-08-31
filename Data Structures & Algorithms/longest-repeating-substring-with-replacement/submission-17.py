class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_hashmap = defaultdict(int)
        start_index = 0
        end_index = 0
        longest_substr = 0

        while end_index < len(s):
            freq_hashmap[s[end_index]] = 1 + freq_hashmap.get(s[end_index], 0)
            current_substr_len = end_index - start_index + 1

            if current_substr_len - max(freq_hashmap.values()) > k:
                freq_hashmap = defaultdict(int)
                current_substr_len = 0
                start_index += 1
                end_index = start_index
            else:
                end_index += 1

            longest_substr = max(longest_substr,current_substr_len)

        return longest_substr
        
            