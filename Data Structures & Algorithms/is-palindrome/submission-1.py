class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for char in s:
            if char.isalnum():
                temp += char.lower()
        return "".join(reversed(temp)) == temp

        