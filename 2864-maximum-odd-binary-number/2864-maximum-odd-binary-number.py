class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeroes_count, ones_count = 0, -1
        
        for bit in s:
            if bit == "0":
                zeroes_count += 1
            else:
                ones_count += 1
                
        out = ""
        
        if ones_count > 0:
            while ones_count > 0:
                out += "1"
                ones_count -= 1
           
        while zeroes_count > 0:
            out += "0"
            zeroes_count -= 1
            
        return out + '1'
        