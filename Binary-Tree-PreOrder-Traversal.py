# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
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
        
        stack.append(root)
        
        while(len(stack)):
            
            #Top element from the stack
            current = stack[len(stack) - 1]
            
            stack.pop()
            
            final_list.append(current.val)
                
            if current.right:
                stack.append(current.right)
        
            if current.left:
                stack.append(current.left)
            
        
        
        
    
        
        