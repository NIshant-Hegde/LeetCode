class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for l in image:
            l.reverse()
            
        for k in image:
            for j in range(len(k)):
                if k[j] == 0:
                    k[j] = 1
                else:
                    k[j] = 0
                    
        return image
                    