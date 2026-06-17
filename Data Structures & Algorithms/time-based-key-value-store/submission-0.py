class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((value,timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds or not self.ds[key]:
            return ""
        l,r = 0,len(self.ds[key])-1
        while l<=r:
            m = l + (r-l)//2
            v,t = self.ds[key][m]
            if t == timestamp:
                return v
            if t < timestamp:
                l = m+1
            else:
                r = m-1
        if r>=0:
            return self.ds[key][r][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)