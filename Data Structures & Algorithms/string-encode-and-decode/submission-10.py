class Solution:

    # Think about edge cases. Like empty list. Like you're testing.

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lens = [str(len(w)) for w in strs]
        first = ",".join(lens)
        return f"{first}_{''.join(strs)}"

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        first, sent = s.split("_",1)
        ans = []
        lens = first.split(",")
        i = 0
        for l in lens:
            ans.append(sent[i:i + int(l)])
            i = i + int(l)
        return ans

