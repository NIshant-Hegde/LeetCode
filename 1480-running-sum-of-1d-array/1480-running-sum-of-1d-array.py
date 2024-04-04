class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        
        for i in range(len(nums)):
            out.append(sum(nums[0:(i+1)]))
        
        return out
            