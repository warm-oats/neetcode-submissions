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
                substr_hashmap[s[r]] = 1 + substr_hashmap.get(s[r], 0)
                
                if conversions_needed < k:
                    r += 1
                elif conversions_needed == k:
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





            



