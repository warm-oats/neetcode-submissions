class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_p = 0
        end_p = len(s) - 1

        while start_p <= end_p:
            while start_p < end_p and not s[start_p].isalnum():
                start_p += 1
            
            while start_p < end_p and not s[end_p].isalnum():
                end_p -= 1

            if s[start_p].lower() != s[end_p].lower():
                return False
            
            start_p += 1
            end_p -= 1

        return True