class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (position, time to reach target)
        tuples = [(position[i], (target - position[i])/speed[i]) for i in range(len(speed))]
        tuples.sort(key = lambda x:x[0])
        stack = []
        for i in range(len(speed)-1, -1, -1):
            if stack:
                (position,time) = stack[-1]
                (positionC,timeC) = tuples[i]
                if timeC <= time:
                    continue
            stack.append(tuples[i])
        return len(stack)
            


        