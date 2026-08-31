class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        substr_hashmap = defaultdict(int)
        longest_repeat_substr = 0

        while r < len(s) and l < len(s):
            if not substr_hashmap.values():
                substr_hashmap[s[r]] = 1
                r += 1
                longest_repeat_substr = max(longest_repeat_substr,sum(substr_hashmap.values()))
            else:
                substr_count = substr_hashmap.values()
                conversions_needed = sum(substr_count) - max(substr_count)
                
                if conversions_needed < k:
                    substr_hashmap[s[r]] += 1
                    r += 1
                elif conversions_needed == k:
                    substr_hashmap[s[r]] += 1
                    new_conversions_needed = sum(substr_count) - max(substr_count)

                    if new_conversions_needed > k:
                        longest_repeat_substr = max(longest_repeat_substr,sum(substr_hashmap.values()) - 1)
                        substr_hashmap = defaultdict(int) 
                        l += 1
                        r = l 
                    else:
                        r += 1

                longest_repeat_substr = max(longest_repeat_substr,sum(substr_hashmap.values()))

        return longest_repeat_substr





            



