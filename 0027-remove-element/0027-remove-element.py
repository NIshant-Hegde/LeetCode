class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        k = 0
        
        for ele in nums:
            if ele != val:
                temp.append(ele)
                k += 1
                
        k1 = k
        
        for i in range(len(nums)):
            if k > 0:
                nums[i] = temp[i]
                k -= 1
            else:
                nums[i] = 0
        
        return k1