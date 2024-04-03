class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        k = 0
        for i in range(0, 2*len(nums)):
            if i == (len(nums)):
                k = i
            ans.append(nums[i - k])
        return ans