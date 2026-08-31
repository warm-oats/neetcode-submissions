class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_hashmap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            freq_hashmap[s[r]] = 1 + freq_hashmap.get(s[r], 0)

            while (r - l + 1) - max(freq_hashmap.values()) > k:
                freq_hashmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res





            



