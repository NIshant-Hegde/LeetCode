class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1 
        s = 0
        
        while lp < rp:
            s = numbers[lp] + numbers[rp]
            if s > target:
                rp-=1
            elif s < target:
                lp+=1
            else:
                 return [lp+1, rp+1]
            
        
        