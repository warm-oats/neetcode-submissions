class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        
        letters_s = defaultdict(int)
        letters_t = defaultdict(int)

        for letter in s:
            letters_s[letter] += 1

        for letter in t:
            letters_t[letter] += 1

        for letter in letters_s:
            if letters_s[letter] != letters_t[letter]:
                return False

        return True

        






