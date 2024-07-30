from typing import List

class Solution:
    def solve(self,i,j,mat,n,ans,move,visited):
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        
        ##downwards
        if i+1<n and not visited[i+1][j] and mat[i+1][j]==1:
            visited[i][j] = 1
            self.solve(i+1,j,mat,n,ans,move+"D",visited)
            visited[i][j] = 0
            
        ##left
        if j-1 >=0 and not visited[i][j-1] and mat[i][j-1]==1:
            visited[i][j] = 1
            self.solve(i,j-1,mat,n,ans,move+"L",visited)
            visited[i][j] = 0
            
            
        ##right
        if(j+1<n and not visited[i][j+1] and mat[i][j+1]==1):
            visited[i][j] = 1
            self.solve(i,j+1,mat,n,ans,move+"R",visited)
            visited[i][j] = 0
            
        #up
        if(i-1 >=0 and not visited[i-1][j] and mat[i-1][j]==1):
            visited[i][j] = 1
            self.solve(i-1,j,mat,n,ans,move+"U",visited)
            visited[i][j] = 0
    def findPath(self, m: List[List[int]]) -> List[str]:
        ans = []
        n = len(m)
        visited = []
        for _ in range(n):
            row = [0] * n
            visited.append(row)
        
        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", visited)
        return ans

#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends