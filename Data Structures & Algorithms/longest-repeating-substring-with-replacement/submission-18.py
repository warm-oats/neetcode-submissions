class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        longest_substr_count = 1

        start_index = 0
        end_index = 0

        while start_index < len(s) and end_index < len(s):
            freq_map[s[end_index]] = 1 + freq_map.get(s[end_index],0)

            if (end_index - start_index + 1) - max(freq_map.values()) <= k:
                longest_substr_count = max(longest_substr_count,end_index - start_index + 1)
                
                if end_index < len(s):
                    end_index += 1
                else:
                    start_index += 1
                    end_index = start_index
                    freq_map = {} 
            else:
                start_index += 1
                end_index = start_index
                freq_map = {} 
        
        return longest_substr_count

            

        