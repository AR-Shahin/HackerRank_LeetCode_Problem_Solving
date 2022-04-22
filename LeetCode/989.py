class Solution:
    def addToArrayForm(self, num, k):
        temp = ''.join(str(e) for e in num)
        sum = int(temp) + k
        converted_num = str(sum)
        
        return list(converted_num)
        
        



s = Solution();

num = [2,7,4]
k = 181

print(s.addToArrayForm(num,k))
