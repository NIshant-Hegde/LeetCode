class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        sum_i = nums[0]
        out.append(sum_i)
        
        for i in range(1, len(nums)):
            sum_i += nums[i]
            out.append(sum_i)
        
        return out
            