class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_index = 0
        end_index = len(s) - 1

        while start_index < len(s):
            if s[start_index].lower() == s[end_index].lower():
                start_index += 1
                end_index -= 1
            elif not s[start_index].isalnum():
                start_index += 1
            elif not s[end_index].isalnum():
                end_index -= 1
            else:
                return False
        
        return True
            