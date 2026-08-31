class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if  len(s2) < len(s1):
            return False

        s1_freq_hashmap = defaultdict(int)

        for char in s1:
            s1_freq_hashmap[char] = 1 + s1_freq_hashmap.get(char, 0)

        l, r = 0, 0
        s2_freq_hashmap = defaultdict(int)

        while l < len(s2) and r < len(s2):
            if s2[r] not in s1_freq_hashmap:
                l += 1
                r = l
                s2_freq_hashmap = defaultdict(int)
            elif len(s1) >= (r - l + 1):
                s2_freq_hashmap[s2[r]] = 1 + s2_freq_hashmap.get(s2[r], 0)
                r += 1

                if s2_freq_hashmap[s2[r - 1]] > s1_freq_hashmap[s2[r - 1]]:
                    l += 1
                    r = l
                    s2_freq_hashmap = defaultdict(int)
            
            if len(s1) < (r - l + 1):
                return True

        return False


                