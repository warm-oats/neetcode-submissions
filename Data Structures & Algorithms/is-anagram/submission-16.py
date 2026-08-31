class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        ana_dict = defaultdict(int)

        for letter in s:
            ana_dict[letter] += 1

        for letter in t:
            if letter not in ana_dict or ana_dict[letter] != t.count(letter):
                return False

        return True