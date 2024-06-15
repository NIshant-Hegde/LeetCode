class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i, ele in enumerate(nums):
            if ele in seen:
                return True
            else:
                seen.add(ele)
        
        return False