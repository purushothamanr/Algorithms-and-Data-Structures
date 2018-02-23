# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        final_list = []
    
        if not root:
            return final_list
        
        self.levelOrder_Recursive(root, final_list)
        
        return final_list
        
    def levelOrder_Recursive(self, root, final_list):
        
        current = root
        
        q = collections.deque()
        
        prev = 1
        
        q.append([current, prev])
        
        temp_list = []

        while(len(q)):
            
            current = q.popleft()
            
            #print(prev, current[1])
            #print(temp_list)
            if prev == current[1]:
                temp_list.append(current[0].val)
            else:
                final_list.append(temp_list)
                temp_list = []
                temp_list.append(current[0].val)
                prev = current[1]
            
            if current[0].left:
                q.append([current[0].left, current[1]+1])
            
            if current[0].right:
                q.append([current[0].right, current[1]+1])
                
        final_list.append(temp_list)

            