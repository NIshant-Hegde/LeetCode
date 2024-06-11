class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hmap = [0] * 3000
        
        n1 = set()
        n2 = set()
        
        for ele in nums1:
            n1.add(ele)
            
        for ele in nums2:
            n2.add(ele) 
        
        for ele in n1:
            hmap[ele + 1000] += 1
            
        for ele in n2:
            hmap[ele + 1000] += 1
            
        out1 = []
        out2 = []
        
        for ele in n1:
            if hmap[ele + 1000] == 1:
                out1.append(ele)
         
        for ele in n2:
            if hmap[ele + 1000] == 1:
                out2.append(ele)
                
        return [out1, out2]