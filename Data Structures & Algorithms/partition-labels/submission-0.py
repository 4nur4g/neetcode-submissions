class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_ind_map = {}
        for ind,char in enumerate(s):
            end_ind_map[char] = ind
        count = 0
        end_ind = 0
        res = []
        for ind,char in enumerate(s):
            end_ind = max(end_ind_map[char], end_ind)
            count += 1
            if end_ind == ind:
                res.append(count)
                count = 0

        return res