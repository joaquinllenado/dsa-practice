# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            node = q.popleft()
            if self.isSame(node, subRoot) == True: return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False

    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if (root and not subRoot) or (subRoot and not root) or (root.val != subRoot.val): return False
        return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)