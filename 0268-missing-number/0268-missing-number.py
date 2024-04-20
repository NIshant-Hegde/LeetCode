def search(l, target, start, end):
    if start > end:
        return -1

    mid = (start + end)//2

    if l[mid] == target:
        return mid
    elif l[mid] < target:
        return search(l, target, mid + 1, end)
    else:
        return search(l, target, start, mid - 1)
    
class Solution:        
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        first = 0
        last = len(nums) - 1
        
        for i in range(0, len(nums) + 1):
            if search(nums, i, first, last) == -1:
                return i