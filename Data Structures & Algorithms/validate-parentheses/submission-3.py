class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        close_dict = {'(':')','{':'}','[':']'}
        for b in s:
            if b in close_dict.keys():
                q.append(b)
            else:
                if not q:
                    return False
                top = q.pop()
                if close_dict[top] != b:
                    return False
        return False if q else True
        