class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftarr = [0] * len(nums)
        rightarr = [0] * len(nums)
        
        leftsum, rightsum = 0, 0
        out = []
        
        for i in range(0, len(nums)):
            leftarr[i] = leftsum
            leftsum += nums[i]
            
            rightarr[-(i+1)] = rightsum
            rightsum += nums[-(i+1)]
            
        for i in range(len(leftarr)):
            out.append(abs(leftarr[i] - rightarr[i]))
            
        return out
            