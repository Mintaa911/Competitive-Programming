class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col = 0,0
        m,n = len(matrix)-1,len(matrix[0])-1
        output = []
        
        while m>=row and n>=col:
            for i in range(col,n+1):
                output.append(matrix[row][i])
            row +=1
            if m < row:
                break
            for j in range(row,m+1):
                output.append(matrix[j][n])
            n -= 1
            if n < col:
                break
            for i in range(n,col-1,-1):
                output.append(matrix[m][i])
            m -= 1
            if m < row:
                break
            for j in range(m,row-1,-1):
                output.append(matrix[j][col])
            col += 1
        return output
            