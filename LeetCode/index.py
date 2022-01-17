# Bruteforce
class Solution:
    def isSameTree(self, p, q):
        is_same = False
        if len(p) == len(q):
            for i in range(0, len(p)):
                if p[i] == q[i]:
                    is_same = True
                else:
                    is_same = False

        return is_same


ob = Solution()
p = [1, 2]
q = [1, None, 2]

print(ob.isSameTree(p, q))
