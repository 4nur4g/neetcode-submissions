class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum() and i < j:
                i += 1
            while j > -1 and not s[j].isalnum() and i < j:
                j -= 1
            if -1 < i < len(s) and -1 < j < len(s) and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


        