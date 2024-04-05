class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        out = 0
        for hour in hours:
            if hour >= target:
                out += 1
        
        return out