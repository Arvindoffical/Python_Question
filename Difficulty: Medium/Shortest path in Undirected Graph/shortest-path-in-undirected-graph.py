#User function Template for python3

from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # 📒 Step 1: Create the adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Because the graph is undirected
        
        # 🚥 Step 2: Prepare for BFS
        dist = [-1] * n  # Distance to all nodes initialized to -1
        dist[src] = 0    # Distance to source is 0
        queue = deque([src])
        
        # 🏃‍♂️ Step 3: BFS
        while queue:
            node = queue.popleft()
            current_dist = dist[node]
            
            for neighbor in graph[node]:
                if dist[neighbor] == -1:  # If neighbor has not been visited
                    dist[neighbor] = current_dist + 1
                    queue.append(neighbor)
        
        # 🎉 Step 4: Return the distances
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends