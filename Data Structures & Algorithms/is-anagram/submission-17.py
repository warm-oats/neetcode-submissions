class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        ana_hash = [0] * 26

        for i in range(len(s)):
            ana_hash[ord(s[i]) - ord('a')] += 1
            ana_hash[ord(t[i]) - ord('a')] -= 1
        
        for count in ana_hash:
            if count != 0: return False

        return True