class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        upto_sum = [[0]*(m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                r,c = i+1,j+1
                _sum = upto_sum[r-1][c] + upto_sum[r][c-1] - upto_sum[r-1][c-1] + mat[i][j]
                upto_sum[r][c] = _sum

        ans = [[0]*(m) for i in range(n)]
        for r in range(1,n+1):
            for c in range(1,m+1):
                i,j = r, c 
                r1,c1 = max((i-k),0),max((j-k),0)
                r2,c2 = min((i + k),n),min((j+k),m)
                if r1 > 0:
                    r1 -= 1
                if c1 > 0:
                    c1 -= 1
                
                x = upto_sum[r1][c2]
                y = upto_sum[r2][c1]
                z = upto_sum[r1][c1]
                _sum = upto_sum[r2][c2] - x - y + z
                ans[r-1][c-1] = _sum

        return ans
