class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for letter in s:
            letter = ''.join(letter)

            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1

        for letter2 in t:
            letter2 = ''.join(letter2)

            if letter2 not in t_dict:
                t_dict[letter2] = 1
            else:
                t_dict[letter2] += 1

        if (len(s_dict) != len(t_dict)):
            return False

        for letter in s_dict.keys():
            if letter not in t_dict:
                return False
            elif s_dict[letter] != t_dict[letter]:
                return False
        
        return True
