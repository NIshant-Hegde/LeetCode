class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i, ele in enumerate(nums):
            if (target - ele) in nums:
                if nums.index(target - ele) != i:
                    out = [i, nums.index(target - ele)]
                    break
                
        return out
                