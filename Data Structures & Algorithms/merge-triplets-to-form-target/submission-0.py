class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for item in triplets:
            if item[0] > target[0] or item[1] > target[1] or item[2] > target[2]:
                continue
            for ind,val in enumerate(item):
                if val == target[ind]:
                    good.add(ind)
                
        return len(good) == 3
        