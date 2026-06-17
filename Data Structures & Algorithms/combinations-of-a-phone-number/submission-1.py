class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        size = len(digits) 
        sub, res = [], []
        def backtrack(di):
            if di >= size:
                res.append("".join(sub.copy())) if sub else None
                return
            for c in num_map[digits[di]]:
                sub.append(c)
                backtrack(di+1)
                sub.pop()
        backtrack(0)
        return res