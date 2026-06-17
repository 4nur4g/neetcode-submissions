class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start_net_gas = [ gas[i] - cost[i] for i in range(len(gas)) ]

        for ind, num in enumerate(start_net_gas):
            total = 0
            for i in range(ind,len(start_net_gas)):
                total += start_net_gas[i]
                if total < 0:
                    break
                if i == len(start_net_gas) - 1:
                    return ind
        return -1
                
                
                
            


        