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
        
        if not root:
            return final_list
        
        self.iterative_solution(root, final_list)
        
        return final_list
    
    def iterative_solution(self, root, final_list):
        
        stack = []
        dict_local = {}
        current_node = root
        
        while(current_node or len(stack)):
            
            while(current_node):
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack[len(stack) - 1]
            
            if (current_node.right):
                if (current_node.right not in dict_local):
                    current_node = current_node.right
                else:
                    current_node = stack.pop()
                    final_list.append(current_node.val)
                    dict_local[current_node] = 1
                    current_node = None
            else:
                current_node = stack.pop()
                final_list.append(current_node.val)
                dict_local[current_node] = 1
                current_node = None
                
        