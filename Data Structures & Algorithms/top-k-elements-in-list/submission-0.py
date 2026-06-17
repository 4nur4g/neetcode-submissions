class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
          freqMap[num] = freqMap.get(num,0) + 1
        ourStore = [[] for i in range(len(nums) + 1)]
        for num, freq in freqMap.items():
            ourStore[freq].append(num)
        result = []
        for i in range(len(ourStore)-1,0,-1):
            for num in ourStore[i]:
                result.append(num)
                if len(result) == k:
                    return result


        