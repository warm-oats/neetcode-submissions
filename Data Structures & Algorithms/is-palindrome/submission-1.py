class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_start = 0
        pointer_end = len(s) - 1

        while (pointer_start < len(s)):
            if not s[pointer_start].isalnum():
                pointer_start += 1
            elif not s[pointer_end].isalnum():
                pointer_end -= 1
            elif s[pointer_start].lower() != s[pointer_end].lower():
                return False
            else:
                pointer_start += 1
                pointer_end -= 1
        
        return True


        