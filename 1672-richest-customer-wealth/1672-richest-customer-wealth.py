class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richestWealth = 0
        for i in range(len(accounts[0])):
            richestWealth += accounts[0][i]
            
        for acc in accounts:
            if sum(acc) > richestWealth:
                richestWealth = sum(acc)
        
        return richestWealth