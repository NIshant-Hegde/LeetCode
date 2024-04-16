class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {"type": 0, "color": 1, "name": 2}
        count = 0
        
        for item in items:
            for i, ele in enumerate(item):
                if (item[rule[ruleKey]] == ruleValue) and i==rule[ruleKey]:
                    count += 1
                    
        return count