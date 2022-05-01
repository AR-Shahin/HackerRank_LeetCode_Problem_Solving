class Solution:
    def maximumWealth(self, accounts):
        
        temp = []
        for row in accounts:
            temp.append(sum(row))

        m = max(temp)
        
        return m

            
s = Solution();

accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]
print(s.maximumWealth(accounts))
