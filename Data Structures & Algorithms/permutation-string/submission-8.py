class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if  len(s2) < len(s1):
            return False

        s1_freq_hashmap = defaultdict(int)

        for char in s1:
            s1_freq_hashmap[char] = 1 + s1_freq_hashmap.get(char, 0)

        for l in range(len(s2)):
            s2_freq_hashmap = defaultdict(int)
            r = l
            
            while r < len(s2) and s2[r] in s1_freq_hashmap:
                s2_freq_hashmap[s2[r]] = 1 + s2_freq_hashmap.get(s2[r], 0)

                if s2_freq_hashmap[s2[r]] > s1_freq_hashmap[s2[r]]:
                    break
                else:
                    r += 1

                    if len(s1) < (r - l + 1):
                        return True

        return False


                