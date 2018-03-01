class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        final_list = []

        if not matrix:
            return final_list
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        top = 0
        bottom = row_len - 1
        
        left = 0
        right = col_len - 1
        
        
        while left <= right and top <= bottom:
            
            for i in range(left, right+1):
                final_list.append(matrix[top][i])
            
            for i in range(top+1,bottom):
                final_list.append(matrix[i][right])
                 
            for i in reversed(range(left,right+1)):
                if top < bottom:
                    final_list.append(matrix[bottom][i])
            
            for i in reversed(range(top+1, bottom)):
                if left < right:
                    final_list.append(matrix[i][left])
                    
            top+= 1
            bottom-=1
            left+=1
            right-=1
            
        return final_list
        