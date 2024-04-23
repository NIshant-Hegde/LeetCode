class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        out = [0, gain[0]]
        alt = gain[0]
        
        for i in range(1, len(gain)):
            alt += gain[i]
            out.append(alt)
            
        return max(out)
        