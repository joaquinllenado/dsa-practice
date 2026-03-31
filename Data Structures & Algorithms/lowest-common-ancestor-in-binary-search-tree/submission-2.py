# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        lca = 0

        while queue:
            node = queue.popleft()

            if p.val < node.val and q.val < node.val:
                lca = node
                queue.append(node.left)
            elif p.val > node.val and q.val > node.val:
                lca = node
                queue.append(node.right)
            else:
                lca = node
                break
        
        return lca