class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        turns = len(nums)//2
        out = []
        
        nums.sort()
        
        i, j = 0, 1
        while turns > 0:
            out.append(nums[j])
            out.append(nums[i])
            i, j = i+2, j+2
            turns-=1
            
        return out