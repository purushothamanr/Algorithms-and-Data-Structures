# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final_list = []
        
        if not root:
            return final_list
        
        self.iterative_solution(root, final_list)
        
        return final_list
    
    def iterative_solution(self, root, final_list):
        
        stack = []
        current_node = root
        
        while(current_node or len(stack)):
            
            while(current_node):
                stack.append(current_node)
                current_node =current_node.left
            
            current_node = stack.pop()
            final_list.append(current_node.val)
            current_node = current_node.right
        
        
        