class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_list_s = list(s)
        str_list_t = list(t)

        str_list_s.sort()
        str_list_t.sort()

        return str_list_s == str_list_t