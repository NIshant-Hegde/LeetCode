class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        
        for i, value in enumerate(nums):
            if (target - value) in seen:
                return [i, nums.index(target - value)]
            else:
                seen.add(value)