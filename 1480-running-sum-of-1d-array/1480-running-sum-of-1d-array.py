class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        sum_i = 0
        
        for i in range(len(nums)):
            sum_i += nums[i]
            out.append(sum_i)
        
        return out
            