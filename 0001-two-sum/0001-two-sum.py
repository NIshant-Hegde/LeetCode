class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, ele in enumerate(nums):
            if (target - ele) in seen:
                return [i, seen[target - ele]]
            else:
                seen[ele] = i
                