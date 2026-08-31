class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_dict,t_dict = defaultdict(int),defaultdict(int)

        for letter in s:
            s_dict[letter] += 1

        for letter in t:
            if letter not in s:
                return False
            elif s_dict[letter] == 0:
                return False
            else:
                s_dict[letter] -= 1
        
        return True





