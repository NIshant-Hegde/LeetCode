class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict(int)
        
        for n in nums:
            freqDict[n] += 1
            
        Keys = list(freqDict.keys())
        Values = list(freqDict.values())
        
        out = []
        while k > 0:
            ind = Values.index(max(Values))
            out.append(Keys[ind])
            Values[ind] = -1
            k-=1
            
        return out