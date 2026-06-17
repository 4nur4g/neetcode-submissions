class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        indStack = []
        for i in range(len(temperatures)-1,-1,-1):
            while indStack and temperatures[indStack[-1]] <= temperatures[i]:
                indStack.pop()
            if indStack and temperatures[indStack[-1]] > temperatures[i]:
                res[i] = indStack[-1] - i
            indStack.append(i)
        return res


                    

        