class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        size = len(s)
        # Initialise dp
        # 0 -> empty, 1 -> first digit
        dp = [0] * (size + 1)
        dp[0] = dp[1] = 1 

        for i in range(2, size+1):
            right_most = s[i-1]
            two_digits = s[i-2:i]
            if right_most in "123456789":
                dp[i] += dp[i-1]
            if int(two_digits) <= 26 and two_digits[0] != "0":
                dp[i] += dp[i-2]
        
        return dp[-1]



        