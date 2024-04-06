class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        out = []
        
        if len(mountain) < 3:
            return out
        else:
            for i in range(2, len(mountain)):
                if (mountain[i - 1] > mountain[i]) and (mountain[i - 1] > mountain[i - 2]):
                    out.append(i - 1)
            return out