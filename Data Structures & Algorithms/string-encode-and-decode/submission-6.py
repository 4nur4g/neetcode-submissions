class Solution:

    def encode(self, strs: List[str]) -> str:
        markers = [len(word) for word in strs]
        return f"{','.join(map(str, markers))}_{''.join(strs)}"

    def decode(self, s: str) -> List[str]:
        if not s or s == "_":
            return []
        marker_section, rem = s.split("_",1)
        markers = list(map(int,marker_section.split(",")))
        res = []
        i = 0
        for m in markers:
            res.append(rem[i:i+m])
            i += m
        return res
            
        

            

