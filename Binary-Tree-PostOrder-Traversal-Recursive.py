# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        final_list = []
        
        self.recursive_solution(root, final_list)
        
        return final_list
    
    def recursive_solution(self, root, final_list):
        
        if not root:
            return
        
        self.recursive_solution(root.left, final_list)
        self.recursive_solution(root.right, final_list)
        
        final_list.append(root.val)
        