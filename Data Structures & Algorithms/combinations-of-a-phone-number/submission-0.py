class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        strings = [digitToChar[n] for n in digits]
        res, track = [],[]
        def backtrack(stri):
            if stri >= len(digits) :
                res.append("".join(track))
                return
            for j in range(len(strings[stri])):
                track.append(strings[stri][j])
                backtrack(stri + 1)
                track.pop()
        backtrack(0)
        return res
        