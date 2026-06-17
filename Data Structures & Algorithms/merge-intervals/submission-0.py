class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        prev = intervals[0]
        res = []
        for n in range(1,len(intervals)):
            if prev[1] < intervals[n][0]:
                res.append(prev)
                prev = intervals[n]
            else:
                prev = [min(prev[0],intervals[n][0]), max(prev[1], intervals[n][1])]
        res.append(prev)
        return res

        