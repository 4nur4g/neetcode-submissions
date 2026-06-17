class Solution:

    def encode(self, strs: List[str]) -> str:
        markers = [len(word) for word in strs]
        return "(" + ",".join(map(str,markers)) + ")" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "()":
            return []
        markers = []
        i = 1
        j = 1

        while s[j] != ")":
            if s[j] == ",":
                markers.append(int(s[i:j]))
                i = j + 1
                j = i
            j += 1
       
        markers.append(int(s[i:j]))
        rem = s[j+1:len(s)]
        
        i = 0
        res = []
        for m in markers:
            res.append(rem[i:i+m])
            i += m
        return res
            
        

            

