class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car_data = [(p,s) for p,s in zip(position, speed)]
        car_data.sort(reverse=True)
        for p,s in car_data:
            t = (target-p)/s
            if stack and stack[-1] >= t:
                continue
            stack.append(t)
        return len(stack)

        

        
        