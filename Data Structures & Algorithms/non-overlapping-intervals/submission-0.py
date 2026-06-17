class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 1:
            return 0
        prev = intervals[0]
        res = 0
        for n in range(1,len(intervals)):
            if prev[1] > intervals[n][0]:
                res += 1
                prev = [max(prev[0],intervals[n][0]),min(prev[1],intervals[n][1])]
            else:
                prev = intervals[n]
        return res

        