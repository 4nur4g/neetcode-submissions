class Solution:

    def encode(self, strs: List[str]) -> str:
        markers = [len(word) for word in strs]
        return "(" + ",".join(map(str,markers)) + ")" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s or s == "()":
            return []
        marker_section, rem = s[1:].split(")",1)
        markers = list(map(int,marker_section.split(",")))
        res = []
        i = 0
        for m in markers:
            res.append(rem[i:i+m])
            i += m
        return res
            
        

            

