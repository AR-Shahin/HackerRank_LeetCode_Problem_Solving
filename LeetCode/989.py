class Solution:
    def checkStraightLine(self,coordinates):
        
        a = coordinates[0]
        b = coordinates[1]
        c = coordinates[2]
        d = coordinates[3]
        e = coordinates[4]
        f = coordinates[5]
        
        s1 = (b[1] - a[1] / b[0] - a[0])
        s2 = (d[1] - c[1] / d[0] - c[0])
        s3 = (f[1] - e[1] / f[0] - e[0])
        
        return True if s1 == s2 == s3 else False
            
s = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates1 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(s.checkStraightLine(coordinates1))
