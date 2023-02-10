class Solution():
    def maximumValue(self, strs):
        t = []
        for s in strs:
            try:
                a = int(s)
                t.append(a)
            except:
                t.append(len(s))
                
        return max(t)
                
    
        
        
        
s = Solution()
strs = ["alic3","bob","3","4","00000"]

print(s.maximumValue(strs))
