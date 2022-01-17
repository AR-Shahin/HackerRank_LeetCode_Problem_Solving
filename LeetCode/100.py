# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

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
