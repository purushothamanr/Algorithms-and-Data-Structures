class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        
        final_list = [[0 for x in range(n)] for y in range(n)]
        
        row_len = n
        col_len = n
        
        top = 0
        bottom = row_len - 1
        
        left = 0
        right = col_len - 1
        
        count = 0
        while left<=right and top <= bottom:
            for i in range(left,right+1):
                count+=1
                final_list[top][i] = count
            
            for i in range(top+1, bottom):
                count+=1
                final_list[i][right] = count
            
            for i in reversed(range(left,right+1)):
                if top < bottom:
                    count+=1
                    final_list[bottom][i] = count
            
            for i in reversed(range(top+1, bottom)):
                if left < right:
                    count+=1
                    final_list[i][left] = count
            
            top+=1
            bottom-=1
            
            left+=1
            right-=1
        
        return final_list
            