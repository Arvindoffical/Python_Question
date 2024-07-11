from typing import List


class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        # code here
        visited = set()
        m, n, d = len(grid), len(grid[0]), {}
        
        def dfs(r, c, s):
            nonlocal m, n
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            if (r, c) in visited:
                return 
            
            visited.add((r, c))
            s.add((r, c))
            d[r, c] = s
            dfs(r+1, c, s)
            dfs(r-1, c, s)
            dfs(r, c-1, s)
            dfs(r, c+1, s)
        
        zeros = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    zeros.append((r, c))
                elif (r, c) not in visited:
                    dfs(r, c, set())

        if not zeros:
            return m*n
            
        ans = 1
        for r, c in zeros:
            ss = []
            cnt = 1
            for r0, c0 in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (r0, c0) not in d:
                    continue
                s0 = d[r0, c0]
               
                for s in ss:
                    if s0 is s:
                        break
                else:
                    ss.append(s0)
                    cnt += len(s0)
                
            ans = max(ans, cnt)
        return ans
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends