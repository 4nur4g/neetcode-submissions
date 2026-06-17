class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        word = ""

        for i in range(len(s)):
            l = i
            r = i
            # for odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > res_len:
                    word = s[l:r+1]
                    res_len = len(s[l:r+1])
                l -= 1
                r += 1
            # for even
            l = i
            r = l + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > res_len:
                    word = s[l:r+1]
                    res_len = len(s[l:r+1])
                l -= 1
                r += 1
        return word

        