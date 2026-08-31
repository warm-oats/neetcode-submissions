class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash = defaultdict(int)

        for char in s1:
            s1_hash[char] = 1 + s1_hash.get(char,0)

        l = 0

        for r in range(len(s2)):

            s1_hash[s2[r]] = s1_hash.get(s2[r],0) - 1

            while s1_hash[s2[r]] < 0:
                s1_hash[s2[l]] += 1
                l += 1
            
            if len(s1) == (r - l + 1):
                return True

            r += 1
        
        return False